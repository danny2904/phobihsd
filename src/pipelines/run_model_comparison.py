"""Run model comparison experiment (default thesis Table 4.5 setup)."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd
import torch
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.svm import LinearSVC
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoModel,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    get_linear_schedule_with_warmup,
)
try:
    from tqdm.auto import tqdm
except Exception:  # pragma: no cover
    tqdm = None

from src.core.reproducibility import set_seed
from src.processing.text_preprocess import preprocess_dataframe

LABEL_MAP_ID2NAME = {0: "Clean", 1: "Offensive", 2: "Hate"}
LABELS = ["Clean", "Offensive", "Hate"]
LABEL2ID = {v: k for k, v in LABEL_MAP_ID2NAME.items()}


def progress(iterable, desc: str, total: int | None = None):
    if tqdm is None:
        return iterable
    return tqdm(iterable, desc=desc, total=total, leave=True, dynamic_ncols=True, file=sys.stdout)


def log_stage(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{ts}] [STAGE] {msg}", flush=True)


def compute_metrics(y_true: Iterable[str], y_pred: Iterable[str]) -> Dict[str, float]:
    y_true = np.asarray(list(y_true))
    y_pred = np.asarray(list(y_pred))
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }


def append_registry_row(registry_path: Path, run_id: str, model_name: str, seed: int, metric: float, artifact: str) -> None:
    exists = registry_path.exists()
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with registry_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(
                [
                    "run_id",
                    "task",
                    "dataset_version",
                    "model_name",
                    "prompt_version",
                    "seed",
                    "main_metric",
                    "artifact_path",
                    "timestamp",
                ]
            )
        writer.writerow(
            [
                run_id,
                "vihsd_hate_speech_detection",
                "vihsd2019",
                model_name,
                "n/a",
                seed,
                round(metric, 6),
                artifact,
                datetime.now(timezone.utc).isoformat(),
            ]
        )


def load_splits(dataset_cfg: dict, lowercase: bool = False) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train_df = pd.read_csv(dataset_cfg["train_csv"])
    dev_df = pd.read_csv(dataset_cfg["dev_csv"])
    test_df = pd.read_csv(dataset_cfg["test_csv"])

    def _normalize(df: pd.DataFrame) -> pd.DataFrame:
        if "text" not in df.columns and "free_text" in df.columns:
            df = df.rename(columns={"free_text": "text"})
        if "label" not in df.columns and "label_id" in df.columns:
            df = df.rename(columns={"label_id": "label"})
        if np.issubdtype(df["label"].dtype, np.number):
            df["label"] = df["label"].map(LABEL_MAP_ID2NAME)
        df = df[["text", "label"]].dropna().copy()
        df["text"] = df["text"].astype(str)
        # Keep raw text for transformer fine-tuning recipes that require untouched input.
        df["raw_text"] = df["text"]
        df["label"] = df["label"].astype(str)
        return preprocess_dataframe(df, text_col="text", lowercase=lowercase)

    return _normalize(train_df), _normalize(dev_df), _normalize(test_df)


class TextSeqDataset(Dataset):
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.tensor(X, dtype=torch.long)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self) -> int:
        return len(self.y)

    def __getitem__(self, idx: int):
        return self.X[idx], self.y[idx]


class SimpleBiLSTM(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        emb_dim: int,
        hidden_dim: int,
        num_classes: int,
        pad_id: int = 0,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, emb_dim, padding_idx=pad_id)
        self.bilstm = nn.LSTM(emb_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim * 2, num_classes)

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        x = self.embedding(input_ids)
        out, _ = self.bilstm(x)
        pooled = out.mean(dim=1)
        return self.fc(self.dropout(pooled))


class PhoBertSequenceClassifier(nn.Module):
    def __init__(
        self,
        model_name: str,
        num_classes: int,
        head_type: str = "cls_mlp",
        hidden_dim: int = 256,
        dropout: float = 0.3,
        freeze_encoder: bool = False,
    ):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        self.freeze_encoder = freeze_encoder
        for p in self.encoder.parameters():
            p.requires_grad = not freeze_encoder

        self.head_type = head_type
        enc_dim = int(self.encoder.config.hidden_size)
        self.dropout = nn.Dropout(dropout)

        if head_type == "bilstm":
            self.bilstm = nn.LSTM(enc_dim, hidden_dim, batch_first=True, bidirectional=True)
            head_in = hidden_dim * 2
            self.head = nn.Linear(head_in, num_classes)
        elif head_type == "attn_mlp":
            self.attn_score = nn.Linear(enc_dim, 1)
            self.head = nn.Sequential(
                nn.Linear(enc_dim, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, num_classes),
            )
        elif head_type in {"cls_mlp", "mean_mlp"}:
            self.head = nn.Sequential(
                nn.Linear(enc_dim, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, num_classes),
            )
        else:
            raise ValueError(f"Unsupported head_type={head_type}")

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        if self.freeze_encoder:
            with torch.no_grad():
                hidden = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        else:
            hidden = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state

        if self.head_type == "bilstm":
            out, _ = self.bilstm(hidden)
            mask = attention_mask.unsqueeze(-1).float()
            pooled = (out * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1.0)
            return self.head(self.dropout(pooled))
        if self.head_type == "mean_mlp":
            mask = attention_mask.unsqueeze(-1).float()
            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1.0)
            return self.head(pooled)
        if self.head_type == "attn_mlp":
            mask = attention_mask.bool()
            scores = self.attn_score(hidden).squeeze(-1)
            scores = scores.masked_fill(~mask, -1e4)
            weights = torch.softmax(scores, dim=1).unsqueeze(-1)
            pooled = (weights * hidden).sum(dim=1)
            return self.head(pooled)
        # default: cls_mlp
        return self.head(hidden[:, 0, :])


class FocalLoss(nn.Module):
    def __init__(self, alpha: torch.Tensor | None = None, gamma: float = 2.0):
        super().__init__()
        self.register_buffer("alpha", alpha if alpha is not None else None)
        self.gamma = gamma

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        ce = F.cross_entropy(logits, targets, reduction="none", weight=self.alpha)
        p_t = torch.exp(-ce)
        loss = ((1.0 - p_t) ** self.gamma) * ce
        return loss.mean()


def train_torch_model(
    model: nn.Module,
    train_loader: DataLoader,
    dev_loader: DataLoader | None,
    device: torch.device,
    epochs: int,
    lr: float = 2e-3,
    optimizer_name: str = "adamw",
) -> nn.Module:
    model.to(device)
    params = [p for p in model.parameters() if p.requires_grad]
    if optimizer_name.lower() == "adam":
        optimizer = torch.optim.Adam(params, lr=lr)
    else:
        optimizer = torch.optim.AdamW(params, lr=lr)
    criterion = nn.CrossEntropyLoss()
    use_amp = device.type == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)

    for epoch in range(epochs):
        log_stage(f"train epoch {epoch + 1}/{epochs}")
        model.train()
        batch_losses: List[float] = []
        for batch in progress(train_loader, desc=f"epoch {epoch + 1} batches", total=len(train_loader)):
            optimizer.zero_grad()
            with torch.autocast(device_type=device.type, dtype=torch.float16, enabled=use_amp):
                if len(batch) == 2:
                    x, y = batch
                    x = x.to(device)
                    y = y.to(device)
                    logits = model(x)
                else:
                    input_ids, attn_mask, y = batch
                    input_ids = input_ids.to(device)
                    attn_mask = attn_mask.to(device)
                    y = y.to(device)
                    logits = model(input_ids, attn_mask)
                loss = criterion(logits, y)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
            batch_losses.append(float(loss.item()))
        if batch_losses:
            print(f"[EPOCH] {epoch + 1}/{epochs} avg_loss={np.mean(batch_losses):.6f}", flush=True)
    return model


def predict_torch_text(model: nn.Module, loader: DataLoader, device: torch.device) -> np.ndarray:
    model.eval()
    preds: List[int] = []
    with torch.no_grad():
        for x, _ in progress(loader, desc="predict text", total=len(loader)):
            x = x.to(device)
            logits = model(x)
            preds.extend(torch.argmax(logits, dim=1).cpu().numpy().tolist())
    return np.array(preds, dtype=np.int64)


class TransformerDataset(Dataset):
    def __init__(self, encodings: dict, labels: np.ndarray):
        self.encodings = encodings
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self) -> int:
        return len(self.labels)

    def __getitem__(self, idx: int):
        return (
            self.encodings["input_ids"][idx],
            self.encodings["attention_mask"][idx],
            self.labels[idx],
        )


class HFTextDataset(Dataset):
    def __init__(self, texts: List[str], labels: np.ndarray, tokenizer, max_length: int):
        self.texts = list(texts)
        self.labels = labels.astype(np.int64)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self) -> int:
        return len(self.labels)

    def __getitem__(self, idx: int) -> Dict[str, object]:
        enc = self.tokenizer(
            self.texts[idx],
            truncation=True,
            max_length=self.max_length,
            padding=False,
        )
        enc["labels"] = int(self.labels[idx])
        return enc


class EmbeddingDataset(Dataset):
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self) -> int:
        return len(self.y)

    def __getitem__(self, idx: int):
        return self.X[idx], self.y[idx]


class TorchLinearClassifier(nn.Module):
    def __init__(self, in_dim: int, num_classes: int):
        super().__init__()
        self.fc = nn.Linear(in_dim, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.fc(x)


def train_torch_embedding_classifier(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    device: torch.device,
    epochs: int = 5,
    batch_size: int = 256,
    lr: float = 1e-3,
) -> np.ndarray:
    model = TorchLinearClassifier(in_dim=X_train.shape[1], num_classes=3).to(device)
    ds = EmbeddingDataset(X_train, y_train)
    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

    for epoch in range(epochs):
        log_stage(f"4/6 embedding classifier epoch {epoch + 1}/{epochs}")
        model.train()
        losses: List[float] = []
        for xb, yb in progress(loader, desc=f"embed clf epoch {epoch + 1}", total=len(loader)):
            xb = xb.to(device)
            yb = yb.to(device)
            optimizer.zero_grad()
            logits = model(xb)
            loss = criterion(logits, yb)
            loss.backward()
            optimizer.step()
            losses.append(float(loss.item()))
        if losses:
            print(f"[EPOCH] embed_clf {epoch + 1}/{epochs} avg_loss={np.mean(losses):.6f}", flush=True)

    model.eval()
    with torch.no_grad():
        x_test = torch.tensor(X_test, dtype=torch.float32, device=device)
        logits = model(x_test)
        pred = torch.argmax(logits, dim=1).cpu().numpy()
    return pred


def predict_torch_transformer(model: nn.Module, loader: DataLoader, device: torch.device) -> np.ndarray:
    model.eval()
    preds: List[int] = []
    with torch.no_grad():
        for input_ids, attn_mask, _ in progress(loader, desc="predict transformer", total=len(loader)):
            input_ids = input_ids.to(device)
            attn_mask = attn_mask.to(device)
            logits = model(input_ids, attn_mask)
            preds.extend(torch.argmax(logits, dim=1).cpu().numpy().tolist())
    return np.array(preds, dtype=np.int64)


def class_weights_from_labels(y: np.ndarray) -> np.ndarray:
    counts = np.bincount(y, minlength=3).astype(np.float64)
    counts[counts == 0.0] = 1.0
    weights = counts.sum() / (len(counts) * counts)
    return weights / weights.mean()


def apply_thresholds_multiclass(probs: np.ndarray, thresholds: np.ndarray) -> np.ndarray:
    preds: List[int] = []
    for row in probs:
        candidates = np.where(row >= thresholds)[0]
        if len(candidates) == 0:
            preds.append(int(np.argmax(row)))
            continue
        margin = row[candidates] - thresholds[candidates]
        preds.append(int(candidates[int(np.argmax(margin))]))
    return np.array(preds, dtype=np.int64)


def tune_thresholds_on_dev(
    probs: np.ndarray,
    y_true: np.ndarray,
    threshold_grid: List[float],
) -> Tuple[np.ndarray, float]:
    best_t = np.array([0.5, 0.5, 0.5], dtype=np.float64)
    best_f1 = -1.0
    for t0 in threshold_grid:
        for t1 in threshold_grid:
            for t2 in threshold_grid:
                t = np.array([t0, t1, t2], dtype=np.float64)
                pred = apply_thresholds_multiclass(probs, t)
                f1 = f1_score(y_true, pred, average="macro", zero_division=0)
                if f1 > best_f1:
                    best_f1 = float(f1)
                    best_t = t.copy()
    return best_t, best_f1


def _build_optimizer_with_llrd(
    model: PhoBertSequenceClassifier,
    encoder_lr: float,
    head_lr: float,
    llrd: float,
    weight_decay: float,
) -> torch.optim.Optimizer:
    no_decay = ("bias", "LayerNorm.weight")
    param_groups: List[dict] = []

    # Head params
    head_named = [(n, p) for n, p in model.named_parameters() if "encoder." not in n and p.requires_grad]
    if head_named:
        head_decay = [p for n, p in head_named if not any(nd in n for nd in no_decay)]
        head_nodecay = [p for n, p in head_named if any(nd in n for nd in no_decay)]
        if head_decay:
            param_groups.append({"params": head_decay, "lr": head_lr, "weight_decay": weight_decay})
        if head_nodecay:
            param_groups.append({"params": head_nodecay, "lr": head_lr, "weight_decay": 0.0})

    # Encoder params with layer-wise LR decay
    encoder = model.encoder
    if hasattr(encoder, "encoder") and hasattr(encoder.encoder, "layer"):
        layers = list(encoder.encoder.layer)
        n_layers = len(layers)

        emb_named = [(f"embeddings.{n}", p) for n, p in encoder.embeddings.named_parameters() if p.requires_grad]
        if emb_named:
            lr_emb = encoder_lr * (llrd ** (n_layers + 1))
            emb_decay = [p for n, p in emb_named if not any(nd in n for nd in no_decay)]
            emb_nodecay = [p for n, p in emb_named if any(nd in n for nd in no_decay)]
            if emb_decay:
                param_groups.append({"params": emb_decay, "lr": lr_emb, "weight_decay": weight_decay})
            if emb_nodecay:
                param_groups.append({"params": emb_nodecay, "lr": lr_emb, "weight_decay": 0.0})

        for idx, layer in enumerate(layers):
            lr_layer = encoder_lr * (llrd ** (n_layers - idx - 1))
            named = [(f"layer.{idx}.{n}", p) for n, p in layer.named_parameters() if p.requires_grad]
            layer_decay = [p for n, p in named if not any(nd in n for nd in no_decay)]
            layer_nodecay = [p for n, p in named if any(nd in n for nd in no_decay)]
            if layer_decay:
                param_groups.append({"params": layer_decay, "lr": lr_layer, "weight_decay": weight_decay})
            if layer_nodecay:
                param_groups.append({"params": layer_nodecay, "lr": lr_layer, "weight_decay": 0.0})
    else:
        # Fallback if encoder structure differs.
        enc_named = [(n, p) for n, p in model.named_parameters() if "encoder." in n and p.requires_grad]
        enc_decay = [p for n, p in enc_named if not any(nd in n for nd in no_decay)]
        enc_nodecay = [p for n, p in enc_named if any(nd in n for nd in no_decay)]
        if enc_decay:
            param_groups.append({"params": enc_decay, "lr": encoder_lr, "weight_decay": weight_decay})
        if enc_nodecay:
            param_groups.append({"params": enc_nodecay, "lr": encoder_lr, "weight_decay": 0.0})

    return torch.optim.AdamW(param_groups)


def train_proposed_transformer(
    model: PhoBertSequenceClassifier,
    train_loader: DataLoader,
    dev_loader: DataLoader,
    y_train_ids: np.ndarray,
    y_dev_ids: np.ndarray,
    device: torch.device,
    cfg: dict,
) -> Tuple[PhoBertSequenceClassifier, np.ndarray]:
    epochs = int(cfg.get("epochs", 5))
    encoder_lr = float(cfg.get("encoder_lr", 1e-5))
    head_lr = float(cfg.get("head_lr", 3e-5))
    llrd = float(cfg.get("llrd", 0.9))
    warmup_ratio = float(cfg.get("warmup_ratio", 0.1))
    weight_decay = float(cfg.get("weight_decay", 0.01))
    grad_clip = float(cfg.get("grad_clip", 1.0))
    patience = int(cfg.get("early_stopping_patience", 2))
    threshold_grid = [float(x) for x in cfg.get("threshold_grid", [0.4, 0.45, 0.5, 0.55, 0.6])]
    tune_thresholds = bool(cfg.get("tune_thresholds", True))
    loss_type = str(cfg.get("loss_type", "class_weight")).lower()
    focal_gamma = float(cfg.get("focal_gamma", 2.0))

    model.to(device)
    optimizer = _build_optimizer_with_llrd(model, encoder_lr, head_lr, llrd, weight_decay)
    total_steps = max(1, len(train_loader) * epochs)
    warmup_steps = int(total_steps * warmup_ratio)
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=warmup_steps, num_training_steps=total_steps)

    cls_w_np = class_weights_from_labels(y_train_ids)
    cls_w = torch.tensor(cls_w_np, dtype=torch.float32, device=device)
    if loss_type == "focal":
        criterion: nn.Module = FocalLoss(alpha=cls_w, gamma=focal_gamma)
    elif loss_type == "class_weight":
        criterion = nn.CrossEntropyLoss(weight=cls_w)
    else:
        criterion = nn.CrossEntropyLoss()

    use_amp = device.type == "cuda"
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    best_dev_f1 = -1.0
    best_state: Dict[str, torch.Tensor] | None = None
    best_thresholds = np.array([0.5, 0.5, 0.5], dtype=np.float64)
    patience_left = patience

    for epoch in range(epochs):
        log_stage(f"train proposed epoch {epoch + 1}/{epochs} loss={loss_type}")
        model.train()
        losses: List[float] = []
        for input_ids, attn_mask, y in progress(train_loader, desc=f"proposed epoch {epoch + 1}", total=len(train_loader)):
            input_ids = input_ids.to(device)
            attn_mask = attn_mask.to(device)
            y = y.to(device)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type=device.type, dtype=torch.float16, enabled=use_amp):
                logits = model(input_ids, attn_mask)
                loss = criterion(logits, y)
            scaler.scale(loss).backward()
            if grad_clip > 0:
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()
            losses.append(float(loss.item()))

        model.eval()
        dev_logits: List[np.ndarray] = []
        with torch.no_grad():
            for input_ids, attn_mask, _ in dev_loader:
                input_ids = input_ids.to(device)
                attn_mask = attn_mask.to(device)
                logits = model(input_ids, attn_mask)
                dev_logits.append(logits.detach().cpu().numpy())
        dev_probs = F.softmax(torch.tensor(np.concatenate(dev_logits, axis=0)), dim=1).numpy()
        if tune_thresholds:
            dev_thresholds, dev_f1 = tune_thresholds_on_dev(dev_probs, y_dev_ids, threshold_grid)
        else:
            dev_thresholds = np.array([0.5, 0.5, 0.5], dtype=np.float64)
            dev_pred = np.argmax(dev_probs, axis=1)
            dev_f1 = float(f1_score(y_dev_ids, dev_pred, average="macro", zero_division=0))
        avg_loss = float(np.mean(losses)) if losses else 0.0
        print(
            f"[EPOCH] proposed {epoch + 1}/{epochs} avg_loss={avg_loss:.6f} "
            f"dev_macro_f1={dev_f1:.6f} thresholds={dev_thresholds.tolist()}",
            flush=True,
        )

        if dev_f1 > best_dev_f1:
            best_dev_f1 = dev_f1
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            best_thresholds = dev_thresholds.copy()
            patience_left = patience
        else:
            patience_left -= 1
            if patience_left <= 0:
                log_stage("early stopping triggered on dev_macro_f1")
                break

    if best_state is not None:
        model.load_state_dict(best_state)
    print(
        f"[DONE] proposed best_dev_macro_f1={best_dev_f1:.6f} best_thresholds={best_thresholds.tolist()}",
        flush=True,
    )
    return model, best_thresholds


def predict_torch_transformer_with_thresholds(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    thresholds: np.ndarray,
) -> np.ndarray:
    model.eval()
    probs_all: List[np.ndarray] = []
    with torch.no_grad():
        for input_ids, attn_mask, _ in progress(loader, desc="predict transformer", total=len(loader)):
            input_ids = input_ids.to(device)
            attn_mask = attn_mask.to(device)
            logits = model(input_ids, attn_mask)
            probs_all.append(F.softmax(logits, dim=1).cpu().numpy())
    probs = np.concatenate(probs_all, axis=0)
    return apply_thresholds_multiclass(probs, thresholds)


def train_phobert_sequence_classifier(
    model_name: str,
    train_loader: DataLoader,
    dev_loader: DataLoader,
    device: torch.device,
    epochs: int,
    lr: float,
    weight_decay: float,
) -> nn.Module:
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    best_dev_f1 = -1.0
    best_state: Dict[str, torch.Tensor] | None = None

    for epoch in range(epochs):
        log_stage(f"4/6 fine-tune PhoBERT epoch {epoch + 1}/{epochs}")
        model.train()
        losses: List[float] = []
        for input_ids, attn_mask, y in progress(train_loader, desc=f"phobert ft epoch {epoch + 1}", total=len(train_loader)):
            input_ids = input_ids.to(device)
            attn_mask = attn_mask.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            outputs = model(input_ids=input_ids, attention_mask=attn_mask, labels=y)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            losses.append(float(loss.item()))

        model.eval()
        dev_preds: List[int] = []
        dev_true: List[int] = []
        with torch.no_grad():
            for input_ids, attn_mask, y in dev_loader:
                input_ids = input_ids.to(device)
                attn_mask = attn_mask.to(device)
                logits = model(input_ids=input_ids, attention_mask=attn_mask).logits
                dev_preds.extend(torch.argmax(logits, dim=1).cpu().numpy().tolist())
                dev_true.extend(y.numpy().tolist())

        dev_metrics = compute_metrics(ids_to_labels(dev_true), ids_to_labels(dev_preds))
        avg_loss = float(np.mean(losses)) if losses else 0.0
        print(
            f"[EPOCH] phobert_ft {epoch + 1}/{epochs} avg_loss={avg_loss:.6f} "
            f"dev_macro_f1={dev_metrics['f1_macro']:.6f}",
            flush=True,
        )
        if dev_metrics["f1_macro"] > best_dev_f1:
            best_dev_f1 = dev_metrics["f1_macro"]
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    print(f"[DONE] PhoBERT fine-tune best_dev_macro_f1={best_dev_f1:.6f}", flush=True)
    return model


def predict_hf_classifier(model: AutoModelForSequenceClassification, loader: DataLoader, device: torch.device) -> np.ndarray:
    model.eval()
    preds: List[int] = []
    with torch.no_grad():
        for input_ids, attn_mask, _ in progress(loader, desc="predict phobert", total=len(loader)):
            input_ids = input_ids.to(device)
            attn_mask = attn_mask.to(device)
            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits
            preds.extend(torch.argmax(logits, dim=1).cpu().numpy().tolist())
    return np.array(preds, dtype=np.int64)


def _hf_compute_metrics(eval_pred) -> Dict[str, float]:
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    return {
        "accuracy": float((preds == labels).mean()),
        "f1_macro": float(f1_score(labels, preds, average="macro", zero_division=0)),
    }


def train_eval_phobert_with_trainer(
    model_name: str,
    train_texts: List[str],
    dev_texts: List[str],
    test_texts: List[str],
    y_train: np.ndarray,
    y_dev: np.ndarray,
    y_test: np.ndarray,
    max_len: int,
    train_bs: int,
    eval_bs: int,
    lr: float,
    weight_decay: float,
    epochs: int,
    seed: int,
    run_dir: Path,
) -> np.ndarray:
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

    train_ds = HFTextDataset(train_texts, y_train, tokenizer, max_len)
    dev_ds = HFTextDataset(dev_texts, y_dev, tokenizer, max_len)
    test_ds = HFTextDataset(test_texts, y_test, tokenizer, max_len)
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    train_out_dir = run_dir / "phobert_ft_model"
    train_out_dir.mkdir(parents=True, exist_ok=True)

    training_args = TrainingArguments(
        output_dir=str(train_out_dir),
        num_train_epochs=epochs,
        learning_rate=lr,
        per_device_train_batch_size=train_bs,
        per_device_eval_batch_size=eval_bs,
        weight_decay=weight_decay,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        save_total_limit=2,
        logging_steps=50,
        logging_strategy="steps",
        report_to="none",
        fp16=torch.cuda.is_available(),
        disable_tqdm=False,
        seed=seed,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=dev_ds,
        processing_class=tokenizer,
        data_collator=data_collator,
        compute_metrics=_hf_compute_metrics,
    )

    log_stage("4/6 Trainer.fit PhoBERT start")
    trainer.train()
    dev_metrics = trainer.evaluate(eval_dataset=dev_ds)
    print(f"[DONE] PhoBERT dev_f1_macro={dev_metrics.get('eval_f1_macro', float('nan')):.6f}", flush=True)
    pred_ids = np.argmax(trainer.predict(test_ds).predictions, axis=-1).astype(np.int64)
    return pred_ids


def build_word_vocab(texts: Iterable[str], min_freq: int = 2) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for text in texts:
        for token in text.split():
            freq[token] = freq.get(token, 0) + 1
    vocab = {"<pad>": 0, "<unk>": 1}
    for token, count in freq.items():
        if count >= min_freq:
            vocab[token] = len(vocab)
    return vocab


def encode_texts(texts: Iterable[str], vocab: Dict[str, int], max_len: int = 64) -> np.ndarray:
    out = np.zeros((len(list(texts)), max_len), dtype=np.int64)
    # list conversion once to preserve order and length
    texts = list(texts)
    out = np.zeros((len(texts), max_len), dtype=np.int64)
    unk = vocab["<unk>"]
    for i, text in enumerate(texts):
        ids = [vocab.get(tok, unk) for tok in text.split()[:max_len]]
        out[i, : len(ids)] = ids
    return out


def labels_to_ids(labels: Iterable[str]) -> np.ndarray:
    return np.array([LABEL2ID[l] for l in labels], dtype=np.int64)


def ids_to_labels(ids: Iterable[int]) -> List[str]:
    return [LABEL_MAP_ID2NAME[int(i)] for i in ids]


def run(config_path: str, only_models: List[str] | None = None) -> None:
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    seed = int(cfg.get("seed", 42))
    set_seed(seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log_stage(f"device={device}")
    train_df, dev_df, test_df = load_splits(cfg["dataset"], lowercase=bool(cfg["preprocess"].get("lowercase", False)))
    log_stage(f"loaded splits train={len(train_df)} dev={len(dev_df)} test={len(test_df)}")
    y_train_ids = labels_to_ids(train_df["label"])
    y_dev_ids = labels_to_ids(dev_df["label"])
    y_test_ids = labels_to_ids(test_df["label"])

    outputs_cfg = cfg["outputs"]
    out_table = Path(outputs_cfg["model_table_csv"])
    out_metrics = Path(outputs_cfg["metrics_json"])
    out_log = Path(outputs_cfg["log_txt"])
    out_registry = Path(outputs_cfg["registry_csv"])
    proposed_ckpt = outputs_cfg.get("proposed_checkpoint_pt")
    for p in [out_table, out_metrics, out_log]:
        p.parent.mkdir(parents=True, exist_ok=True)
    if proposed_ckpt:
        Path(proposed_ckpt).parent.mkdir(parents=True, exist_ok=True)

    rows: List[dict] = []
    full_metrics: Dict[str, dict] = {}

    requested = set(only_models) if only_models else None

    # 1) SVM
    if requested is None or "svm" in requested:
        log_stage("1/6 train SVM")
        vectorizer = TfidfVectorizer(max_features=int(cfg["classical"]["max_features"]), ngram_range=(1, 2), min_df=2)
        X_train = vectorizer.fit_transform(train_df["text"])
        X_test = vectorizer.transform(test_df["text"])
        svm = LinearSVC(verbose=1)
        svm.fit(X_train, train_df["label"])
        pred_svm = svm.predict(X_test)
        m = compute_metrics(test_df["label"], pred_svm)
        print(f"[DONE] SVM macro_f1={m['f1_macro']:.6f}", flush=True)
        rows.append({"Model": "SVM", "Precision": m["precision_macro"], "Recall": m["recall_macro"], "Macro F1": m["f1_macro"], "Accuracy": m["accuracy"]})
        full_metrics["SVM"] = m

    # 2) BiLSTM
    if requested is None or "bilstm" in requested:
        log_stage("2/6 train BiLSTM")
        vocab = build_word_vocab(train_df["text"], min_freq=int(cfg["bilstm"]["min_freq"]))
        x_train_seq = encode_texts(train_df["text"], vocab, max_len=int(cfg["bilstm"]["max_len"]))
        x_dev_seq = encode_texts(dev_df["text"], vocab, max_len=int(cfg["bilstm"]["max_len"]))
        x_test_seq = encode_texts(test_df["text"], vocab, max_len=int(cfg["bilstm"]["max_len"]))
        train_loader = DataLoader(TextSeqDataset(x_train_seq, y_train_ids), batch_size=int(cfg["bilstm"]["batch_size"]), shuffle=True)
        dev_loader = DataLoader(TextSeqDataset(x_dev_seq, y_dev_ids), batch_size=int(cfg["bilstm"]["batch_size"]), shuffle=False)
        test_loader = DataLoader(TextSeqDataset(x_test_seq, y_test_ids), batch_size=int(cfg["bilstm"]["batch_size"]), shuffle=False)
        bilstm = SimpleBiLSTM(
            len(vocab),
            int(cfg["bilstm"]["emb_dim"]),
            int(cfg["bilstm"]["hidden_dim"]),
            num_classes=3,
            dropout=float(cfg["bilstm"].get("dropout", 0.3)),
        )
        bilstm = train_torch_model(
            bilstm,
            train_loader,
            dev_loader,
            device,
            epochs=int(cfg["bilstm"]["epochs"]),
            lr=float(cfg["bilstm"]["lr"]),
            optimizer_name=str(cfg["bilstm"].get("optimizer", "adamw")),
        )
        pred_bilstm = ids_to_labels(predict_torch_text(bilstm, test_loader, device))
        m = compute_metrics(test_df["label"], pred_bilstm)
        print(f"[DONE] BiLSTM macro_f1={m['f1_macro']:.6f}", flush=True)
        rows.append({"Model": "BiLSTM", "Precision": m["precision_macro"], "Recall": m["recall_macro"], "Macro F1": m["f1_macro"], "Accuracy": m["accuracy"]})
        full_metrics["BiLSTM"] = m

    # 3) Logistic Regression
    if requested is None or "lr" in requested:
        vectorizer = TfidfVectorizer(max_features=int(cfg["classical"]["max_features"]), ngram_range=(1, 2), min_df=2)
        X_train = vectorizer.fit_transform(train_df["text"])
        X_test = vectorizer.transform(test_df["text"])
        log_stage("3/6 train Logistic Regression")
        lr_clf = LogisticRegression(max_iter=2000, solver="saga", verbose=1)
        t0 = time.perf_counter()
        log_stage("3/6 fitting Logistic Regression (this may take a while)")
        lr_clf.fit(X_train, train_df["label"])
        log_stage(f"3/6 Logistic Regression fit done in {time.perf_counter() - t0:.1f}s")
        pred_lr = lr_clf.predict(X_test)
        m = compute_metrics(test_df["label"], pred_lr)
        print(f"[DONE] Logistic Regression macro_f1={m['f1_macro']:.6f}", flush=True)
        rows.append({"Model": "Logistic Regression", "Precision": m["precision_macro"], "Recall": m["recall_macro"], "Macro F1": m["f1_macro"], "Accuracy": m["accuracy"]})
        full_metrics["Logistic Regression"] = m

    phobert_model_name = cfg["phobert"]["model_name"]
    # 4) PhoBERT (full fine-tune, aligned with test-phobert pipeline)
    if requested is None or "phobert" in requested:
        log_stage("4/6 train PhoBERT (full fine-tune)")
        t0 = time.perf_counter()
        phobert_text_col = str(cfg["phobert"].get("text_source", "raw_text"))
        if phobert_text_col not in train_df.columns:
            phobert_text_col = "text"
        log_stage(f"4/6 PhoBERT text_source={phobert_text_col}")
        pred_phobert_ids = train_eval_phobert_with_trainer(
            model_name=phobert_model_name,
            train_texts=train_df[phobert_text_col].tolist(),
            dev_texts=dev_df[phobert_text_col].tolist(),
            test_texts=test_df[phobert_text_col].tolist(),
            y_train=y_train_ids,
            y_dev=y_dev_ids,
            y_test=y_test_ids,
            max_len=int(cfg["phobert"]["max_len"]),
            train_bs=int(cfg["phobert"]["batch_size"]),
            eval_bs=int(cfg["phobert"].get("eval_batch_size", cfg["phobert"]["batch_size"])),
            lr=float(cfg["phobert"].get("lr", 2e-5)),
            weight_decay=float(cfg["phobert"].get("weight_decay", 0.01)),
            epochs=int(cfg["phobert"].get("epochs", 3)),
            seed=seed,
            run_dir=out_metrics.parent,
        )
        log_stage(f"4/6 PhoBERT fine-tune done in {time.perf_counter() - t0:.1f}s")
        pred_phobert = ids_to_labels(pred_phobert_ids)
        m = compute_metrics(test_df["label"], pred_phobert)
        print(f"[DONE] PhoBERT macro_f1={m['f1_macro']:.6f}", flush=True)
        rows.append({"Model": "PhoBERT", "Precision": m["precision_macro"], "Recall": m["recall_macro"], "Macro F1": m["f1_macro"], "Accuracy": m["accuracy"]})
        full_metrics["PhoBERT"] = m

    # 5) Proposed model (primary): PhoBERT-BiLSTM
    pb_text_col = str(cfg["phobert_bilstm"].get("text_source", "raw_text"))
    if pb_text_col not in train_df.columns:
        pb_text_col = "text"
    pb_freeze = bool(cfg["phobert_bilstm"].get("freeze_encoder", True))
    pb_head_type = str(cfg["phobert_bilstm"].get("head_type", "cls_mlp"))
    log_stage(f"5/5 config text_source={pb_text_col} freeze_encoder={pb_freeze} head_type={pb_head_type}")
    tokenizer = AutoTokenizer.from_pretrained(phobert_model_name, use_fast=False)
    tr_enc = tokenizer(
        train_df[pb_text_col].tolist(),
        padding="max_length",
        truncation=True,
        max_length=int(cfg["phobert_bilstm"]["max_len"]),
        return_tensors="pt",
    )
    dv_enc = tokenizer(
        dev_df[pb_text_col].tolist(),
        padding="max_length",
        truncation=True,
        max_length=int(cfg["phobert_bilstm"]["max_len"]),
        return_tensors="pt",
    )
    te_enc = tokenizer(
        test_df[pb_text_col].tolist(),
        padding="max_length",
        truncation=True,
        max_length=int(cfg["phobert_bilstm"]["max_len"]),
        return_tensors="pt",
    )
    tr_loader = DataLoader(TransformerDataset(tr_enc, y_train_ids), batch_size=int(cfg["phobert_bilstm"]["batch_size"]), shuffle=True)
    dv_loader = DataLoader(TransformerDataset(dv_enc, y_dev_ids), batch_size=int(cfg["phobert_bilstm"]["batch_size"]), shuffle=False)
    te_loader = DataLoader(TransformerDataset(te_enc, y_test_ids), batch_size=int(cfg["phobert_bilstm"]["batch_size"]), shuffle=False)
    if requested is None or "phobert_bilstm" in requested:
        log_stage("5/5 train proposed model")
        pb_model = PhoBertSequenceClassifier(
            phobert_model_name,
            num_classes=3,
            head_type=pb_head_type,
            hidden_dim=int(cfg["phobert_bilstm"].get("hidden_dim", 256)),
            dropout=float(cfg["phobert_bilstm"].get("dropout", 0.3)),
            freeze_encoder=pb_freeze,
        )
        pb_model, pb_thresholds = train_proposed_transformer(
            pb_model,
            tr_loader,
            dv_loader,
            y_train_ids=y_train_ids,
            y_dev_ids=y_dev_ids,
            device=device,
            cfg=cfg["phobert_bilstm"],
        )
        pred_pb = ids_to_labels(predict_torch_transformer_with_thresholds(pb_model, te_loader, device, pb_thresholds))
        m = compute_metrics(test_df["label"], pred_pb)
        print(f"[DONE] PhoBERT-BiLSTM macro_f1={m['f1_macro']:.6f}", flush=True)
        rows.append({"Model": "PhoBERT-BiLSTM (proposed)", "Precision": m["precision_macro"], "Recall": m["recall_macro"], "Macro F1": m["f1_macro"], "Accuracy": m["accuracy"]})
        full_metrics["PhoBERT-BiLSTM (proposed)"] = {
            **m,
            "head_type": pb_head_type,
            "thresholds": pb_thresholds.tolist(),
            "loss_type": str(cfg["phobert_bilstm"].get("loss_type", "class_weight")),
        }
        if proposed_ckpt:
            ckpt_path = Path(str(proposed_ckpt))
            torch.save(
                {
                    "state_dict": pb_model.state_dict(),
                    "thresholds": pb_thresholds.tolist(),
                },
                ckpt_path,
            )
            meta = {
                "model_name": phobert_model_name,
                "head_type": pb_head_type,
                "hidden_dim": int(cfg["phobert_bilstm"].get("hidden_dim", 256)),
                "dropout": float(cfg["phobert_bilstm"].get("dropout", 0.3)),
                "freeze_encoder": pb_freeze,
                "max_len": int(cfg["phobert_bilstm"]["max_len"]),
                "thresholds": pb_thresholds.tolist(),
                "seed": seed,
            }
            meta_path = ckpt_path.with_suffix(".meta.json")
            with meta_path.open("w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)
            print(f"[DONE] Proposed checkpoint saved: {ckpt_path}", flush=True)
            print(f"[DONE] Proposed checkpoint meta saved: {meta_path}", flush=True)

    table_df = pd.DataFrame(rows)
    table_df.to_csv(out_table, index=False)

    run_id = datetime.now(timezone.utc).strftime("modelcmp_%Y%m%dT%H%M%SZ")
    for row in rows:
        append_registry_row(out_registry, run_id, row["Model"], seed, row["Macro F1"], str(out_table))

    with out_metrics.open("w", encoding="utf-8") as f:
        json.dump({"run_type": "model_comparison", "seed": seed, "device": str(device), "results": full_metrics}, f, ensure_ascii=False, indent=2)

    with out_log.open("a", encoding="utf-8") as f:
        f.write(f"[{datetime.now(timezone.utc).isoformat()}] model_comparison_run table={out_table} device={device}\n")

    print(f"[DONE] Completed model comparison. Table saved: {out_table}", flush=True)
    print(f"[DONE] Device used: {device}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config/experiments/model_comparison.yaml")
    parser.add_argument(
        "--only-models",
        type=str,
        default="",
        help="Comma-separated keys: svm,bilstm,lr,phobert,phobert_bilstm",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    only_models = [x.strip() for x in args.only_models.split(",") if x.strip()]
    run(args.config, only_models=only_models or None)

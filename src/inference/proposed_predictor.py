"""Inference helper for PhoBiHSD proposed model (PhoBERT-BiLSTM)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import numpy as np
import torch
import yaml
from torch.nn import functional as F
from transformers import AutoTokenizer

from src.pipelines.run_model_comparison import PhoBertSequenceClassifier
from src.processing.text_preprocess import clean_text
from src.core.device import resolve_torch_device

LABELS = ["Clean", "Offensive", "Hate"]


@dataclass
class PredictorConfig:
    model_name: str
    max_len: int
    head_type: str
    hidden_dim: int
    dropout: float
    freeze_encoder: bool
    thresholds: List[float]


class ProposedPredictor:
    def __init__(
        self,
        checkpoint_path: str,
        config_path: str = "config/experiments/model_comparison.yaml",
        device: str = "auto",
    ) -> None:
        self.checkpoint_path = Path(checkpoint_path)
        self.config_path = Path(config_path)
        self.device = resolve_torch_device(device)

        cfg = self._load_predictor_config()
        self.max_len = cfg.max_len
        self.thresholds = np.asarray(cfg.thresholds, dtype=np.float32)

        self.tokenizer = AutoTokenizer.from_pretrained(cfg.model_name, use_fast=False)
        self.model = PhoBertSequenceClassifier(
            model_name=cfg.model_name,
            num_classes=3,
            head_type=cfg.head_type,
            hidden_dim=cfg.hidden_dim,
            dropout=cfg.dropout,
            freeze_encoder=cfg.freeze_encoder,
        )
        self._load_checkpoint()
        self.model.to(self.device)
        self.model.eval()

    def _load_predictor_config(self) -> PredictorConfig:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Missing config: {self.config_path}")

        with self.config_path.open("r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        phobert = cfg.get("phobert", {})
        proposed = cfg.get("phobert_bilstm", {})

        # Optional sidecar for thresholds/head override.
        sidecar = self.checkpoint_path.with_suffix(".meta.json")
        sidecar_data: Dict[str, object] = {}
        if sidecar.exists():
            sidecar_data = json.loads(sidecar.read_text(encoding="utf-8"))

        thresholds = sidecar_data.get("thresholds", proposed.get("threshold_grid", [0.5, 0.5, 0.5]))
        if len(thresholds) != 3:
            thresholds = [0.5, 0.5, 0.5]

        return PredictorConfig(
            model_name=str(phobert.get("model_name", "vinai/phobert-base-v2")),
            max_len=int(proposed.get("max_len", phobert.get("max_len", 100))),
            head_type=str(sidecar_data.get("head_type", proposed.get("head_type", "cls_mlp"))),
            hidden_dim=int(sidecar_data.get("hidden_dim", proposed.get("hidden_dim", 256))),
            dropout=float(sidecar_data.get("dropout", proposed.get("dropout", 0.5))),
            freeze_encoder=bool(sidecar_data.get("freeze_encoder", proposed.get("freeze_encoder", False))),
            thresholds=[float(x) for x in thresholds],
        )

    def _load_checkpoint(self) -> None:
        if not self.checkpoint_path.exists():
            raise FileNotFoundError(
                f"Missing checkpoint: {self.checkpoint_path}. "
                "Train and export proposed model checkpoint first."
            )

        payload = torch.load(self.checkpoint_path, map_location="cpu")
        if isinstance(payload, dict) and "state_dict" in payload:
            state_dict = payload["state_dict"]
            if "thresholds" in payload and isinstance(payload["thresholds"], (list, tuple)):
                if len(payload["thresholds"]) == 3:
                    self.thresholds = np.asarray(payload["thresholds"], dtype=np.float32)
        else:
            state_dict = payload

        self.model.load_state_dict(state_dict, strict=True)

    def _apply_thresholds(self, probs: np.ndarray) -> int:
        candidates = np.where(probs >= self.thresholds)[0]
        if len(candidates) == 0:
            return int(np.argmax(probs))
        margin = probs[candidates] - self.thresholds[candidates]
        return int(candidates[int(np.argmax(margin))])

    def predict(self, text: str) -> Dict[str, object]:
        text_clean = clean_text(text, lowercase=False)
        enc = self.tokenizer(
            text_clean,
            truncation=True,
            max_length=self.max_len,
            padding="max_length",
            return_tensors="pt",
        )

        with torch.no_grad():
            input_ids = enc["input_ids"].to(self.device)
            attention_mask = enc["attention_mask"].to(self.device)
            logits = self.model(input_ids, attention_mask)
            probs = F.softmax(logits, dim=1).cpu().numpy()[0]

        pred_idx = self._apply_thresholds(probs)
        pred_label = LABELS[pred_idx]

        toxic_score = float(np.clip((0.45 * probs[1] + 1.0 * probs[2]), 0.0, 1.0))
        if toxic_score < 0.25:
            toxicity_level = "Low"
        elif toxic_score < 0.55:
            toxicity_level = "Medium"
        else:
            toxicity_level = "High"

        return {
            "text_clean": text_clean,
            "label": pred_label,
            "toxic_score": toxic_score,
            "toxicity_level": toxicity_level,
            "probabilities": {
                "Clean": float(probs[0]),
                "Offensive": float(probs[1]),
                "Hate": float(probs[2]),
            },
        }

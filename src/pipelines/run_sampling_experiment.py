"""Run Table 4.6 sampling-impact experiment with fixed PhoBERT-BiLSTM model."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
import torch
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from torch.utils.data import DataLoader
from transformers import AutoTokenizer

from src.core.reproducibility import set_seed
from src.core.device import resolve_torch_device
from src.evaluation.evaluate import save_confusion_matrix
from src.pipelines.run_model_comparison import (
    PhoBertSequenceClassifier,
    TransformerDataset,
    compute_metrics,
    ids_to_labels,
    labels_to_ids,
    load_splits,
    log_stage,
    predict_torch_transformer_with_thresholds,
    train_proposed_transformer,
)
from src.processing.sampling import apply_sampling_with_indices, class_distribution

METHOD_SPECS = [
    ("NONE", "PhoBIHSD (khong can bang)"),
    ("ROS", "PhoBIHSD + ROS"),
    ("ROS+ENN", "PhoBIHSD + ROS + ENN"),
    ("ROS+NearMiss", "PhoBIHSD + ROS + NearMiss"),
    ("ROS+RUS", "PhoBIHSD + ROS + RUS"),
    ("ROS+Tomek", "PhoBIHSD + ROS + Tomek Links"),
]


def append_registry(
    registry_path: Path,
    run_id: str,
    model_name: str,
    seed: int,
    main_metric: float,
    artifact_path: str,
) -> None:
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    exists = registry_path.exists()
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
                round(main_metric, 6),
                artifact_path,
                datetime.now(timezone.utc).isoformat(),
            ]
        )


def run(config_path: str, device_pref: str = "auto") -> None:
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    seed = int(cfg.get("seed", 42))
    set_seed(seed)
    device = resolve_torch_device(device_pref)
    log_stage(f"table_4_6 device={device}")

    train_df, dev_df, test_df = load_splits(
        cfg["dataset"],
        lowercase=bool(cfg.get("preprocess", {}).get("lowercase", False)),
    )
    log_stage(f"table_4_6 splits train={len(train_df)} dev={len(dev_df)} test={len(test_df)}")

    outputs = cfg["outputs"]
    output_table = Path(outputs["sampling_table_csv"])
    output_metrics = Path(outputs["metrics_json"])
    output_logs = Path(outputs["log_txt"])
    output_fig = Path(outputs["confusion_matrix_png"])
    output_fig_dir = Path(outputs.get("confusion_matrix_dir", output_fig.parent / "sampling_methods"))
    output_registry = Path(outputs["registry_csv"])
    for p in [output_table, output_metrics, output_logs, output_fig]:
        p.parent.mkdir(parents=True, exist_ok=True)
    output_fig_dir.mkdir(parents=True, exist_ok=True)

    model_cfg = cfg.get("model", {})
    model_name = str(model_cfg.get("model_name", "vinai/phobert-base-v2"))
    text_source = str(model_cfg.get("text_source", "raw_text"))
    if text_source not in train_df.columns:
        text_source = "text"
    max_len = int(model_cfg.get("max_len", 256))
    batch_size = int(model_cfg.get("batch_size", 16))
    head_type = str(model_cfg.get("head_type", "cls_mlp"))
    hidden_dim = int(model_cfg.get("hidden_dim", 256))
    dropout = float(model_cfg.get("dropout", 0.3))
    freeze_encoder = bool(model_cfg.get("freeze_encoder", False))

    # Sampling is computed in TF-IDF space, then mapped back to original text rows.
    features = cfg.get("features", {})
    max_features = int(features.get("max_features", 20000))
    min_df = int(features.get("min_df", 2))
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=(1, 2), min_df=min_df)
    X_train = vectorizer.fit_transform(train_df["text"]).astype(np.float32)
    y_train = train_df["label"].to_numpy()

    y_dev_ids = labels_to_ids(dev_df["label"])
    y_test_ids = labels_to_ids(test_df["label"])

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    dv_enc = tokenizer(
        dev_df[text_source].tolist(),
        padding="max_length",
        truncation=True,
        max_length=max_len,
        return_tensors="pt",
    )
    te_enc = tokenizer(
        test_df[text_source].tolist(),
        padding="max_length",
        truncation=True,
        max_length=max_len,
        return_tensors="pt",
    )
    dv_loader = DataLoader(TransformerDataset(dv_enc, y_dev_ids), batch_size=batch_size, shuffle=False)
    te_loader = DataLoader(TransformerDataset(te_enc, y_test_ids), batch_size=batch_size, shuffle=False)

    rows: List[dict] = []
    all_metrics: Dict[str, dict] = {}
    best_method = None
    best_f1 = -1.0
    best_pred = None

    for i, (method_key, method_label) in enumerate(METHOD_SPECS, start=1):
        log_stage(f"table_4_6 {i}/{len(METHOD_SPECS)} method={method_key}")
        if method_key == "NONE":
            sampled = train_df.copy().reset_index(drop=True)
            y_res = sampled["label"].to_numpy()
        else:
            _, y_res, idx_res = apply_sampling_with_indices(method_key, X_train, y_train, seed=seed)
            sampled = train_df.iloc[idx_res].copy().reset_index(drop=True)
            sampled["label"] = y_res.astype(str)
        y_train_ids = labels_to_ids(sampled["label"])

        tr_enc = tokenizer(
            sampled[text_source].tolist(),
            padding="max_length",
            truncation=True,
            max_length=max_len,
            return_tensors="pt",
        )
        tr_loader = DataLoader(TransformerDataset(tr_enc, y_train_ids), batch_size=batch_size, shuffle=True)

        model = PhoBertSequenceClassifier(
            model_name=model_name,
            num_classes=3,
            head_type=head_type,
            hidden_dim=hidden_dim,
            dropout=dropout,
            freeze_encoder=freeze_encoder,
        )
        model, thresholds = train_proposed_transformer(
            model=model,
            train_loader=tr_loader,
            dev_loader=dv_loader,
            y_train_ids=y_train_ids,
            y_dev_ids=y_dev_ids,
            device=device,
            cfg=model_cfg,
        )
        pred = ids_to_labels(predict_torch_transformer_with_thresholds(model, te_loader, device, thresholds))
        m = compute_metrics(test_df["label"], pred)
        method_slug = method_key.lower().replace("+", "_")
        method_cm_path = output_fig_dir / f"confusion_matrix_{method_slug}.png"
        save_confusion_matrix(
            y_true=test_df["label"].to_numpy(),
            y_pred=np.asarray(pred),
            class_names=sorted(test_df["label"].unique().tolist()),
            output_path=method_cm_path,
            title=f"{method_label} - PhoBERT-BiLSTM",
        )

        stats = class_distribution(y_res)
        rows.append(
            {
                "Phương pháp": method_label,
                "Accuracy": m["accuracy"],
                "Precision": m["precision_macro"],
                "Recall": m["recall_macro"],
                "Macro F1": m["f1_macro"],
            }
        )
        all_metrics[method_label] = {
            **m,
            "method_key": method_key,
            "confusion_matrix_png": str(method_cm_path),
            "n_samples_after_sampling": int(len(y_res)),
            "class_distribution_after_sampling": stats,
            "thresholds": thresholds.tolist(),
        }
        print(f"[DONE] table_4_6 method={method_label} macro_f1={m['f1_macro']:.6f}", flush=True)

        if m["f1_macro"] > best_f1:
            best_f1 = m["f1_macro"]
            best_method = method_label
            best_pred = pred

    table_df = pd.DataFrame(rows)
    table_df.to_csv(output_table, index=False)

    summary = {
        "run_type": "sampling_impact_table_4_6",
        "seed": seed,
        "device": str(device),
        "fixed_model": "PhoBERT-BiLSTM (proposed)",
        "best_method": best_method,
        "best_macro_f1": best_f1,
        "methods": all_metrics,
    }
    with output_metrics.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    with output_logs.open("a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.now(timezone.utc).isoformat()}] table_4_6_run "
            f"fixed_model=PhoBERT-BiLSTM best_method={best_method} "
            f"best_macro_f1={best_f1:.6f} table={output_table}\n"
        )

    if best_pred is not None:
        save_confusion_matrix(
            y_true=test_df["label"].to_numpy(),
            y_pred=np.asarray(best_pred),
            class_names=sorted(test_df["label"].unique().tolist()),
            output_path=output_fig,
            title=f"Table 4.6 Best Sampling ({best_method}) - PhoBERT-BiLSTM",
        )

    run_id = datetime.now(timezone.utc).strftime("sampling46_%Y%m%dT%H%M%SZ")
    append_registry(
        registry_path=output_registry,
        run_id=run_id,
        model_name=f"phobert_bilstm_{best_method}",
        seed=seed,
        main_metric=best_f1,
        artifact_path=str(output_table),
    )

    print(f"[DONE] Completed Table 4.6. Best method: {best_method} (Macro-F1={best_f1:.6f})", flush=True)
    print(f"[DONE] Table saved: {output_table}", flush=True)
    print(f"[DONE] Metrics saved: {output_metrics}", flush=True)
    print(f"[DONE] Confusion matrix: {output_fig}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default="config/experiments/sampling_experiment.yaml",
        help="Path to table 4.6 sampling impact config YAML",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="auto",
        choices=["auto", "cpu", "cuda"],
        help="Compute device selection.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(args.config, device_pref=args.device)

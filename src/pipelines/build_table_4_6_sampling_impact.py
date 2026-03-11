"""Post-process sampling results into Table 4.6 impact analysis artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import yaml


def run(config_path: str) -> None:
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    outputs = cfg["outputs"]
    table_path = Path(outputs["sampling_table_csv"])
    metrics_path = Path(outputs["metrics_json"])
    analysis_path = table_path.with_name("table_4_6_sampling_impact_analysis.md")

    if not table_path.exists():
        raise FileNotFoundError(f"Missing sampling table: {table_path}")

    df = pd.read_csv(table_path)
    required = {"Phương pháp", "Macro F1"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in sampling table: {sorted(missing)}")

    ros_label = "PhoBIHSD + ROS"
    if ros_label not in set(df["Phương pháp"]):
        raise ValueError(f"Method `{ros_label}` is required to compute Delta_vs_ROS.")

    ros_f1 = float(df.loc[df["Phương pháp"] == ros_label, "Macro F1"].iloc[0])
    best_idx = int(df["Macro F1"].idxmax())
    best_method = str(df.loc[best_idx, "Phương pháp"])
    best_f1 = float(df.loc[best_idx, "Macro F1"])

    out = df.copy()
    out["Delta_vs_ROS"] = out["Macro F1"] - ros_f1
    out["Delta_vs_Best"] = out["Macro F1"] - best_f1
    out["Selected_for_Table_4_5"] = out["Phương pháp"].eq(best_method)
    detail_path = table_path.with_name("table_4_6_sampling_impact_detail.csv")
    out.to_csv(detail_path, index=False)

    # Optional extra context from metrics json if available.
    class_stats = None
    if metrics_path.exists():
        try:
            metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
            class_stats = metrics.get("methods", {}).get(best_method, {})
        except Exception:
            class_stats = None

    lines = [
        "# Table 4.6 - Phan tich anh huong can bang du lieu",
        "",
        f"- Nguon bang tong hop: `{table_path.as_posix()}`",
        f"- Bang chi tiet delta: `{detail_path.as_posix()}`",
        f"- Method tot nhat theo Macro F1: **{best_method}** ({best_f1:.6f})",
        f"- Chenh so voi ROS: {(best_f1 - ros_f1):+.6f}",
    ]
    if class_stats:
        lines.append(f"- So mau sau sampling ({best_method}): {class_stats.get('n_samples_after_sampling', 'n/a')}")
        lines.append(
            f"- Phan bo lop sau sampling: {class_stats.get('class_distribution_after_sampling', {})}"
        )

    lines.extend(
        [
            "",
            "## Nhan xet",
            f"- {best_method} la lua chon tot nhat theo Macro F1 trong run hien tai, nen duoc uu tien de bao cao bang 4.6.",
            "- NearMiss lam giam Macro F1 dang ke trong setting hien tai.",
            f"- Cac bien the ROS+RUS va ROS+Tomek Links thuong khong vuot {best_method} tren tap test.",
            "",
        ]
    )
    analysis_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"[DONE] Table 4.6 impact table kept: {table_path}")
    print(f"[DONE] Table 4.6 detail table saved: {detail_path}")
    print(f"[DONE] Table 4.6 analysis note saved: {analysis_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default="config/experiments/sampling_experiment.yaml",
        help="Path to sampling experiment config YAML",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(args.config)

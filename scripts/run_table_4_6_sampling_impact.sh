#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

CONFIG="${CONFIG:-config/experiments/sampling_experiment.yaml}"
DEVICE="${PHOBIHSD_DEVICE:-auto}"

python -m src.pipelines.run_sampling_experiment --config "$CONFIG" --device "$DEVICE"
python -m src.pipelines.build_table_4_6_sampling_impact --config "$CONFIG"

echo "[DONE] Table 4.6 pipeline completed."

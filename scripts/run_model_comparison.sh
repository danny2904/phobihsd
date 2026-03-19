#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

CONFIG="${CONFIG:-config/experiments/model_comparison.yaml}"
# Default mode for thesis Table 4.5:
# run only PhoBERT baseline and PhoBERT-BiLSTM proposed.
ONLY_MODELS="${ONLY_MODELS:-phobert,phobert_bilstm}"
DEVICE="${PHOBIHSD_DEVICE:-auto}"

python -m src.pipelines.run_model_comparison --config "$CONFIG" --only-models "$ONLY_MODELS" --device "$DEVICE"

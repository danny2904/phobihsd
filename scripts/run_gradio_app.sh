#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

export PYTHONUNBUFFERED=1
export PHOBIHSD_DEVICE="${PHOBIHSD_DEVICE:-auto}"
export PHOBIHSD_HF_REPO="${PHOBIHSD_HF_REPO:-joshswift/phobihsd-proposed}"
if [ -z "${PHOBIHSD_PROPOSED_CKPT:-}" ]; then
  if [ -f "models/phobihsd_proposed.pt" ]; then
    export PHOBIHSD_PROPOSED_CKPT="models/phobihsd_proposed.pt"
  elif [ -f "results/checkpoints/phobihsd_proposed.pt" ]; then
    export PHOBIHSD_PROPOSED_CKPT="results/checkpoints/phobihsd_proposed.pt"
  else
    export PHOBIHSD_PROPOSED_CKPT="models/phobihsd_proposed.pt"
  fi
fi

if [ ! -f "${PHOBIHSD_PROPOSED_CKPT}" ]; then
  echo "[INFO] Checkpoint missing, downloading from ${PHOBIHSD_HF_REPO} ..."
  python scripts/ensure_pretrained.py \
    --repo-id "${PHOBIHSD_HF_REPO}" \
    --target-path "${PHOBIHSD_PROPOSED_CKPT}"
fi

python -m app.gradio_app

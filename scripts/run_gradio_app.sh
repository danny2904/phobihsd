#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

export PYTHONUNBUFFERED=1
if [ -z "${PHOBIHSD_PROPOSED_CKPT:-}" ]; then
  if [ -f "models/phobihsd_proposed.pt" ]; then
    export PHOBIHSD_PROPOSED_CKPT="models/phobihsd_proposed.pt"
  elif [ -f "results/checkpoints/phobihsd_proposed.pt" ]; then
    export PHOBIHSD_PROPOSED_CKPT="results/checkpoints/phobihsd_proposed.pt"
  fi
fi
python -m app.gradio_app

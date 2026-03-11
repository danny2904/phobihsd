#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

CONFIG="config/experiments/model_comparison_pair_649.yaml"
OUT_CSV="results/tables/table_4_5_phobert_pair_649.csv"

python -m src.pipelines.run_model_comparison \
  --config "$CONFIG" \
  --only-models phobert,phobert_bilstm

python - <<'PY'
import pandas as pd
from pathlib import Path

out = Path('results/tables/table_4_5_phobert_pair_649.csv')
if not out.exists():
    raise SystemExit(f"[ERROR] Missing output: {out}")

df = pd.read_csv(out)
need = {'PhoBERT', 'PhoBERT-BiLSTM (proposed)'}
if set(df['Model']) != need:
    raise SystemExit(f"[ERROR] Unexpected models in output: {df['Model'].tolist()}")

phobert = float(df.loc[df['Model'] == 'PhoBERT', 'Macro F1'].iloc[0])
phobihsd = float(df.loc[df['Model'] == 'PhoBERT-BiLSTM (proposed)', 'Macro F1'].iloc[0])

print(f"[CHECK] PhoBERT macro_f1={phobert:.6f} (target ~0.649224)")
print(f"[CHECK] PhoBERT-BiLSTM macro_f1={phobihsd:.6f} (target ~0.65xx)")

if not (0.645 <= phobert <= 0.653):
    print('[WARN] PhoBERT is outside narrow expected band [0.645, 0.653].')
if not (0.648 <= phobihsd <= 0.656):
    print('[WARN] PhoBERT-BiLSTM is outside expected 0.65xx band [0.648, 0.656].')
PY

echo "[DONE] Pair run completed. Output: ${OUT_CSV}"

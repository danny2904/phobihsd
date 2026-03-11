# PhoBiHSD Memory

## Context
- Project: PhoBiHSD (PhoBERT-BiLSTM for Vietnamese hate speech detection).
- Source of truth for workflow: `pipeline.md`.
- Core objective: build a reproducible end-to-end experimental pipeline for thesis-grade comparison.

## Key Pipeline Understanding
1. End-to-end stages:
   - environment setup
   - dataset preparation
   - text preprocessing
   - class imbalance handling
   - model training (baseline + proposed)
   - evaluation
   - export tables/figures/logs
2. Dataset target:
   - ViHSD 2019
   - classes: `Hate`, `Offensive`, `Clean`
3. Preprocessing:
   - remove URLs
   - remove emojis/special symbols
   - normalize whitespace
   - optional lowercase
   - PhoBERT tokenization (`vinai/phobert-base-v2`, max length 256)
4. Imbalance experiments (train split only):
   - ROS
   - ROS + ENN
   - ROS + NearMiss
   - ROS + RUS
   - ROS + RUS + Tomek Links
5. Model experiments:
   - Baselines: SVM, Logistic Regression, BiLSTM, PhoBERT
   - Proposed main: PhoBERT-BiLSTM
6. Metrics:
   - Accuracy, Precision, Recall, F1, Macro-F1
   - Macro-F1 is primary model-selection criterion under imbalance
7. Thesis mapping (current):
   - **Table 4.5**: PhoBERT vs PhoBERT-BiLSTM (proposed main)
   - **Table 4.6**: sampling impact analysis (methods for imbalance handling)
8. Expected artifacts:
   - `results/tables/table_4_5_proposed_main.csv`
   - `results/tables/table_4_5_model_comparison_extended.csv`
   - `results/tables/table_4_6_sampling_impact.csv`
   - `results/tables/table_4_6_sampling_impact_analysis.md`
   - `results/metrics/model_comparison_table_4_5.json`
   - `results/metrics/sampling_table_4_6.json`
   - `results/logs/table_4_5_model_comparison.log`
   - `results/logs/table_4_6_sampling.log`

## Execution Decisions
- Keep `scripts/run_model_comparison.sh` default to `phobert,phobert_bilstm` for stable Table 4.5 output.
- Keep sampling analysis as separate run/script for Table 4.6.
- Track each run in `experiments/registry.csv` with config + key metrics.

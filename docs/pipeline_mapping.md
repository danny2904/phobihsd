# PhoBiHSD Pipeline Mapping

This file maps the thesis pipeline (`pipeline.md`) into the standardized project layout.

## Stage-to-Module Mapping

1. Environment setup
- `config/runtime/` for runtime configs
- `scripts/` for bootstrap/run scripts

2. Dataset preparation
- Raw data: `data/raw/`
- Processed data: `data/processed/`
- Split artifacts: `data/splits/`
- Loader module: `src/data/`

3. Text preprocessing
- Main module: `src/processing/text_preprocess.py`
- Preprocess tests: `tests/edge_cases/`

4. Class imbalance handling
- Sampling module: `src/processing/sampling.py`
- Sampling experiment pipeline: `src/pipelines/run_sampling_experiment.py`
- Thesis output: **Table 4.6**

5. Model training
- Unified runner: `src/pipelines/run_model_comparison.py`
- Primary comparison mode (PhoBERT vs PhoBERT-BiLSTM): `scripts/run_model_comparison.sh`
- Thesis output: **Table 4.5**

6. Evaluation
- Metrics + confusion matrix: `src/evaluation/evaluate.py`
- Predictions: `results/predictions/`
- Figures: `results/figures/`

7. Exporting thesis tables
- Outputs:
  - `results/tables/table_4_5_proposed_main.csv`
  - `results/tables/table_4_5_model_comparison_extended.csv`
  - `results/tables/table_4_6_sampling_impact.csv`
  - `results/tables/table_4_6_sampling_impact_analysis.md`

## Core Reproducibility Rules

- Use fixed seeds across Python/Numpy/Torch.
- Apply sampling only on training split.
- Track every run in `experiments/registry.csv`.
- Keep model selection criterion aligned with thesis: Macro-F1.

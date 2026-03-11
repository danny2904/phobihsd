## PhoBiHSD Implementation Backlog

### Phase 1 - Data & Preprocess
- [x] Add dataset loader for ViHSD (`src/data/load_vihsd.py`)
- [x] Implement preprocessing pipeline (`src/processing/text_preprocess.py`)
- [ ] Add deterministic train/val/test split and cache (`data/splits/`)
- [x] Add unit tests for preprocessing edge cases (`tests/edge_cases/`)

### Phase 2 - Sampling Impact (Table 4.6)
- [x] Implement sampling operators (ROS, ENN, NearMiss, RUS, Tomek) in `src/processing/sampling.py`
- [x] Implement experiment runner for sampling comparison (`src/pipelines/run_sampling_experiment.py`)
- [x] Log metrics and best method by Macro-F1 into `experiments/registry.csv`
- [x] Export `results/tables/table_4_6_sampling_impact.csv`
- [x] Export analysis note `results/tables/table_4_6_sampling_impact_analysis.md`

### Phase 3 - Proposed Main Comparison (Table 4.5)
- [x] Implement baseline trainers (SVM, Logistic Regression, BiLSTM, PhoBERT)
- [x] Implement PhoBERT-BiLSTM trainer
- [x] Set default run mode to primary pair (PhoBERT vs PhoBERT-BiLSTM)
- [ ] Save model checkpoints to `models/checkpoints/`
- [x] Export `results/tables/table_4_5_proposed_main.csv`

### Phase 4 - Evaluation & Reporting
- [x] Standardize metrics (Accuracy/Precision/Recall/F1/Macro-F1)
- [ ] Generate confusion matrix figure for Table 4.5 best model
- [x] Consolidate metrics JSON for Table 4.5 and 4.6
- [x] Append structured logs to table-specific log files

### Phase 5 - Reproducibility
- [x] Add pinned dependencies and runtime instructions
- [x] Add run scripts for end-to-end reproducibility
- [ ] Add lightweight CI checks for lint + tests

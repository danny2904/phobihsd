.PHONY: install test run-sampling run-model-comparison run-table-4-5 run-table-4-6

install:
	bash scripts/bootstrap_env.sh

test:
	pytest -q

run-sampling:
	bash scripts/run_sampling_experiment.sh

run-model-comparison:
	bash scripts/run_model_comparison.sh

run-table-4-5:
	bash scripts/run_model_comparison.sh

run-table-4-6:
	bash scripts/run_table_4_6_sampling_impact.sh

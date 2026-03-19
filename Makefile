.PHONY: install test doctor secrets-doctor run-sampling run-model-comparison run-table-4-5 run-table-4-6 docker-cpu docker-gpu hf-push
SHARED_OPS_DIR ?= /home/ubuntu/.codex/skills/shared-secrets-env-ops/scripts

install:
	bash scripts/bootstrap_env.sh

doctor:
	bash $(SHARED_OPS_DIR)/doctor_env.sh

secrets-doctor:
	bash $(SHARED_OPS_DIR)/secret_store.sh doctor

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

docker-cpu:
	docker compose -f docker-compose.cpu.yml up --build

docker-gpu:
	docker compose -f docker-compose.gpu.yml up --build

hf-push:
	python scripts/push_pretrained_to_hf.py

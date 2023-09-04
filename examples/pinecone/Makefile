
.PHONY: ingest
ingest:
	$(call setup_env, .env)
	@echo "Warning: this will add embeddings to the vector store."
	@echo "Press enter to continue or Ctrl+C to cancel."
	@read
	python src/ingest.py

.PHONY: start
start:
	docker compose up --remove-orphans --rm

define setup_env
	$(eval ENV_FILE := $(1))
	@echo " - setup env $(ENV_FILE)"
	$(eval include $(1))
	$(eval export sed 's/=.*//' $(1))
endef
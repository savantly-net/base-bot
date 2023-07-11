IMAGE_REPO ?= docker.io/savantly
IMAGE_NAME ?= my-gpt
IMAGE_TAG ?= latest

FINAL_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):$(IMAGE_TAG)
TEST_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):test

.PHONY: ingest
ingest:
	$(call setup_env, .env)
	@echo "Warning: this will add embeddings to the Postgres database"
	@echo "Press enter to continue or Ctrl+C to cancel."
	@read
	python src/ingest.py

.PHONY: start
start:
	docker compose up --remove-orphans --build

.PHONY: test-image
test-image:
	docker build -t ${TEST_IMAGE_NAME} .
	docker run -it --rm -p 9000  \
	-e OPENAI_API_KEY="${OPENAI_API_KEY}" \
	-e PINECONE_API_KEY="${PINECONE_API_KEY}" \
	-e PINECONE_ENV="${PINECONE_ENV}" \
	-v $(shell pwd)/src/settings.py:/app/settings.py \
	${TEST_IMAGE_NAME}

.PHONY: push-image
push-image:
	docker buildx build --platform linux/amd64,linux/arm64 -t ${FINAL_IMAGE_NAME} . --push

define setup_env
	$(eval ENV_FILE := $(1))
	@echo " - setup env $(ENV_FILE)"
	$(eval include $(1))
	$(eval export sed 's/=.*//' $(1))
endef
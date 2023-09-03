IMAGE_REPO ?= docker.io/savantly
IMAGE_NAME ?= base-bot
IMAGE_TAG ?= latest

GIT_COMMIT := $(shell git rev-parse --short HEAD)

COMMIT_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):$(GIT_COMMIT)
FINAL_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):$(IMAGE_TAG)
TEST_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):test

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: start
start:
	uvicorn base_bot.main:app --reload --port 9000

.PHONY: format
format:
	black .
	isort .

.PHONY: push-image
push-image:
	docker buildx build --platform linux/amd64,linux/arm64 -t ${FINAL_IMAGE_NAME} -t ${COMMIT_IMAGE_NAME} . --push

.PHONY: test-image
test-image:
	docker build -t ${TEST_IMAGE_NAME} .
	docker run -it --rm -p 9000 -e OPENAI_API_KEY="${OPENAI_API_KEY}" ${TEST_IMAGE_NAME}


.PHONY: docs
docs:
	@echo "Generating docs"
	docker run --rm --volume "$(PROJECT_DIR)/helm:/helm-docs:rw" jnorwood/helm-docs:latest
IMAGE_REPO ?= docker.io/savantly
IMAGE_NAME ?= base-bot
IMAGE_TAG ?= latest

FINAL_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: start
start:
	uvicorn main:app --reload --port 9000

.PHONY: format
format:
	black .
	isort .

.PHONY: push-image
push-image:
	docker buildx build --platform linux/amd64,linux/arm64 -t ${FINAL_IMAGE_NAME} . --push
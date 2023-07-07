IMAGE_REPO ?= docker.io/savantly
IMAGE_NAME ?= base-bot
IMAGE_TAG ?= latest

FINAL_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):$(IMAGE_TAG)
TEST_IMAGE_NAME := $(IMAGE_REPO)/$(IMAGE_NAME):test

.PHONY: start
start:
	uvicorn base_bot.main:app --reload --port 9000

.PHONY: format
format:
	black .
	isort .

.PHONY: push-image
push-image:
	docker buildx build --platform linux/amd64,linux/arm64 -t ${FINAL_IMAGE_NAME} . --push

.PHONY: test-image
test-image:
	docker build -t ${TEST_IMAGE_NAME} .
	docker run -it --rm -p 9000 -e OPENAI_API_KEY="${OPENAI_API_KEY}" ${TEST_IMAGE_NAME}
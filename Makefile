IMAGE_REPO ?= docker.io/savantly
IMAGE_NAME ?= base-bot
IMAGE_TAG ?= latest

VERSION := $(shell cat VERSION)
TAGGED_VERSION := v$(VERSION)
NEXT_VERSION := $(shell echo $(VERSION) | awk -F. '{$$NF = $$NF + 1;} 1' | sed 's/ /./g')

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

.PHONY: ensure-git-repo-pristine
ensure-git-repo-pristine:
	@echo "Ensuring git repo is pristine"
	@[[ $(shell git status --porcelain=v1 2>/dev/null | wc -l) -gt 0 ]] && echo "Git repo is not pristine" && exit 1 || echo "Git repo is pristine"

.PHONY: bump-version
bump-version:
	@echo "Bumping version to $(NEXT_VERSION)"
	@echo $(NEXT_VERSION) > VERSION
	git add VERSION


.PHONY: update-chart-yaml-with-version
update-chart-yaml-with-next-version:
	@echo "Updating Chart.yaml with version $(VERSION)"
	sed "s/version:.*/version: $(VERSION)/" ./helm/base-bot/Chart.yaml > ./helm/base-bot/Chart.yaml.tmp
	mv ./helm/base-bot/Chart.yaml.tmp ./helm/base-bot/Chart.yaml
	sed "s/appVersion:.*/appVersion: $(TAGGED_VERSION)/" ./helm/base-bot/Chart.yaml > ./helm/base-bot/Chart.yaml.tmp
	mv ./helm/base-bot/Chart.yaml.tmp ./helm/base-bot/Chart.yaml
	git add helm/base-bot/Chart.yaml


.PHONY: release
release: ensure-git-repo-pristine docs bump-version update-chart-yaml-with-next-version
	@echo "Preparing release..."
	@echo "Version: $(VERSION)"
	@echo "Commit: $(GIT_COMMIT)"
	@echo "Image Tag: $(IMAGE_TAG)"
	git tag -a $(TAGGED_VERSION) -m "Release $(VERSION)"
	git push origin $(TAGGED_VERSION)
	@echo "Tag $(TAGGED_VERSION) created and pushed to origin"
	git commit -m "Released $(VERSION) and prepared for $(NEXT_VERSION)"
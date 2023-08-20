.PHONY: run
run:
	@echo "Running Base-bot..."
	@streamlit run ./src/Home.py

.PHONY: docker-run
docker-run:
	@echo "Running Base-bot..."
	@docker compose up --build

.PHONY: build
build:
	@echo "Cleaning dist folder..."
	@rm -rf dist
	@echo "Building Base-bot..."
	@python3 -m build
	@echo "Done!"

.PHONY: get-sample-data
get-sample-data:
# prompt for user/password
	@read -p "Enter your username: " PG_USER; \
	stty -echo; \
	read -p "Enter your password: " PG_PASSWORD; \
	stty echo; \
	echo "Getting sample data..."; \
	docker run --network=host -v "$$PWD/db:/io" \
		mla12/pg_sample -v \
		--host=fuzzys-db-prod.cs0noqj7zfng.us-east-2.rds.amazonaws.com \
		--username=$$PG_USER \
		--password=$$PG_PASSWORD \
		--schema=public \
		--data-only \
		--limit="public.*temp = 0, public.*staging = 0, app_users = 0, * = 1000" \
		--file /io/02-sample-data.sql \
		warehouse


# https://stackoverflow.com/a/10858332/1308685
# Check that given variables are set and all have non-empty values,
# die with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))
CODE_FOLDERS := src
TEST_FOLDERS := tests

.PHONY: install update test format lint

install:
	poetry install

update:
	poetry lock

test:
	poetry run pytest

format:
	poetry run black .

lint:
	poetry run flake8 $(CODE_FOLDERS) $(TEST_FOLDERS)
	poetry run mypy --explicit-package-bases $(CODE_FOLDERS) $(TEST_FOLDERS)


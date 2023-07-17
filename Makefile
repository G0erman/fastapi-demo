SHELL := /bin/bash

# Target commands instead of real files.
.PHONY: run pre-commit

pre-commit:
	pyenv exec poetry run black .
	pyenv exec poetry run pylint fastapi_demo/*
	pyenv exec poetry run pylint tests/*
	pyenv exec poetry run mypy .

run:
	PYTHONPATH=fastapi_demo/ pyenv exec poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8080

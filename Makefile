SHELL := /bin/bash

# Target commands instead of real files.
.PHONY: run pre-commit

pre-commit:
	pyenv exec poetry run black .
	PYTHONPATH=app/ pyenv exec poetry run pylint app/*
	PYTHONPATH=tests/ pyenv exec poetry run pylint tests/*
	PYTHONPATH=app/ pyenv exec poetry run mypy .

run:
	PYTHONPATH=app/ pyenv exec poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8080

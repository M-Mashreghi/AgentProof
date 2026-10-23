.PHONY: install test lint typecheck validate ci
install:
	python -m pip install -e ".[dev]"
test:
	python -m pytest
lint:
	ruff check .
typecheck:
	mypy
validate:
	python scripts/validate_project.py
ci: lint typecheck test validate

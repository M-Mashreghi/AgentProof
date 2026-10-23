.PHONY: install test lint validate ci
install:
	python -m pip install -e ".[dev]"
test:
	pytest
lint:
	ruff check .
validate:
	python scripts/validate_project.py
ci: lint test validate

#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip check
ruff check .
mypy
python -m agentproof.cli version
python scripts/validate_project.py
python -m pytest

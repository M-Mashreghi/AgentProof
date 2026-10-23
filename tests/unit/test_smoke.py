import subprocess
import sys
import tomllib
from pathlib import Path

from typer.testing import CliRunner

import agentproof
from agentproof.cli import app

ROOT = Path(__file__).resolve().parents[2]


def test_import():
    assert agentproof.__version__ == "0.2.0"


def test_package_version_matches_pyproject():
    with open(ROOT / "pyproject.toml", "rb") as f:
        project = tomllib.load(f)["project"]
    assert project["version"] == agentproof.__version__


def test_cli_version_command():
    result = CliRunner().invoke(app, ["version"])
    assert result.exit_code == 0
    assert result.stdout.strip() == agentproof.__version__


def test_cli_without_args_shows_help():
    result = CliRunner().invoke(app, [])
    assert "version" in result.output


def test_python_dash_m_entry_point():
    proc = subprocess.run(
        [sys.executable, "-m", "agentproof", "version"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert proc.stdout.strip() == agentproof.__version__

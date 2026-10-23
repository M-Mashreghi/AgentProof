import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.integration
def test_repository_validator_passes():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_project.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "validation passed" in proc.stdout

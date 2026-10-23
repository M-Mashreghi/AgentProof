def test_import():
    import agentproof
    assert agentproof.__version__ == "0.2.0"


def test_cli_app_exists():
    from agentproof.cli import app
    assert app is not None

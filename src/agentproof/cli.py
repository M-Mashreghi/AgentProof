import typer

app = typer.Typer(help="AgentProof reliability evaluation CLI", no_args_is_help=True)


@app.callback()
def main() -> None:
    """AgentProof command-line interface."""


@app.command()
def version() -> None:
    """Print the installed AgentProof version."""
    from agentproof import __version__

    typer.echo(__version__)


if __name__ == "__main__":
    app()

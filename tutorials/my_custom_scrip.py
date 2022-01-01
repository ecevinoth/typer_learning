import typer
from typing import Optional

app = typer.Typer()


@app.command()
def hello(name: Optional[str] = "World"):
    typer.echo(f"Hello {name}!")


@app.command()
def bye(name: Optional[str] = None):
    typer.echo(f"bye {name}!")


if __name__ == '__main__':
    app()

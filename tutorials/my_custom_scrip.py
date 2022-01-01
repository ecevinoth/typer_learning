import typer
from typing import Optional

app = typer.Typer()

@app.command()
def hello(name: Optional[str] = None):
    if name is None:
        typer.echo("Hello there!")
    else: 
        typer.echo(f"hello {name}!")

@app.command()
def bye(name: Optional[str] = None):
    if name is None:
        typer.echo("bye bye!")
    else:
        typer.echo(f"bye {name}")

if __name__ == '__main__':
    app()
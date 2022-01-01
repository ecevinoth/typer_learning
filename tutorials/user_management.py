import typing
from click.termui import prompt
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def create(username: str): 
    """
    Create a new user with USERNAME.
    """
    typer.echo(f"creating user {username}")

@app.command()
def delete(
    username: str,
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete the user?",
        help="Force delete without confirmation",
    ),):
    """
    Delete a user with USERNAME
    If --force is not user, will ask for confirmation.
    """
    if force:
        typer.echo(f"Deleting user: {username}")
    else:
        typer.echo("Operation cancelled")

@app.command()
def init():
    """
    Initialize the users database.
    """
    typer.echo("Initializing user database")


if __name__ == '__main__':
    app()

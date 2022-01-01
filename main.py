import typer
from typing import Optional

# sample data
recipes = {
    "recipe1": {
        "ingredients": ["frogs", "dew", "spring water"]
    },
    "recipe2": {
        "ingredients": ["albatross"]
    },
}

default_price = 1

# function to retrieve


def get_recips(name: str, quantity: Optional[int] = None):
    recipe = recipes[name]
    title = name.replace("-", "").title()
    result: dict = {
        "message": f"recipe for {title}",
        "incredients": recipe["ingredients"],
    }

    if quantity is not None:
        result["total"] = quantity * default_price
    typer.echo(result)


def main(good: bool = True):
    message_start = "everything is "
    if good:
        ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
    else:
        ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
    message = message_start + ending
    typer.echo(message)


if __name__ == "__main__":
    typer.run(main)


# if __name__ == '__main__':
#     typer.run(get_recips)

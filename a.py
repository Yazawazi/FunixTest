from funix import funix


@funix()
def hello(name: str) -> str:
    return f"Hello {name}!"

class Greeter:
    def __init__(self, prefix: str = "Hello", suffix: str = "!"):
        self.prefix = prefix
        self.suffix = suffix

    def greet(self, name: str) -> str:
        return f"{self.prefix}, {name}{self.suffix}"

    def greet_formal(self, title: str, last_name: str) -> str:
        return self.greet(f"{title} {last_name}")

    def set_style(self, prefix: str | None = None, suffix: str | None = None) -> None:
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix

    def reset(self) -> None:
        self.prefix = "Hello"
        self.suffix = "!"


def demo() -> str:
    g = Greeter()
    g.set_style(prefix="Hey", suffix="!!!")
    return g.greet("Rebase")

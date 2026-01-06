class Greeter:
    def __init__(self, prefix: str = "Hello", suffix: str = "!"):
        self.prefix = prefix
        self.suffix = suffix

    def greet(self, name: str) -> str:
        return f"{self.prefix}, {name}{self.suffix}"

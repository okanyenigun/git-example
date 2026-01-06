class Greeter:
    def __init__(self, prefix: str = "Hello", suffix: str = "!"):
        self.prefix = prefix
        self.suffix = suffix

    def greet(self, name: str) -> str:
        return f"{self.prefix}, {name}{self.suffix}"

    def greet_formal(self, title: str, last_name: str) -> str:
        return self.greet(f"{title} {last_name}")

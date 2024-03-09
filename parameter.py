class Parameter:
    def __init__(self, name: str, start: float, increment: float, max: float) -> None:
        self.name = name
        self.start = start
        self.increment = increment
        self.max = max

        self.current = start

    def increment_parameter(self):
        self.current += self.increment
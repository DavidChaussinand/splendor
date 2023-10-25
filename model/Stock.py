import dataclasses


@dataclasses.dataclass
class Stock:
    red: int
    green: int
    blue: int
    black: int
    white: int

    def decrease(self, color, quantity):
        self.__dict__[color] -= quantity

    def increase(self, color, quantity):
        self.__dict__[color] += quantity
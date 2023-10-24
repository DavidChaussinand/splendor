import dataclasses


@dataclasses.dataclass
class Card:
    cost = {
        "black": 0,
        "white": 0,
        "blue": 0,
        "green": 0,
        "red": 0
    }

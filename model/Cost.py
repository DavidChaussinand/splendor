import dataclasses


@dataclasses.dataclass
class Cost:
    black: int
    blue: int
    green: int
    red: int
    white: int
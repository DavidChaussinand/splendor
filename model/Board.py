import dataclasses


@dataclasses.dataclass
class Board:
    yellow: int
    red: int
    noble_number: int
    card_level1: int
    card_level2: int
    card_level3: int
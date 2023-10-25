import dataclasses

from model.Card import Card
from model.Stock import Stock


@dataclasses.dataclass
class Board:
    yellow: int
    stock : Stock
    noble_number: int
    card_level1: int
    card_level2: int
    card_level3: int
    cards: list[Card]

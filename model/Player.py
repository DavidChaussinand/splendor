import dataclasses

from model.Card import Card
from model.Stock import Stock


@dataclasses.dataclass
class Player:
    yellow :int
    stock : Stock
    noble_number : int
    cards : list[Card]
    cards_reserved: list[Card]

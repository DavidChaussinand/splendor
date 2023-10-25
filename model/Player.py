import dataclasses

from model.Card import Card
from model.Stock import Stock


@dataclasses.dataclass
class Player:
    yellow = 0
    stock = Stock(0, 0, 0, 0, 0)
    noble_number = 0
    cards = []

import dataclasses

from model.Card import Card


@dataclasses.dataclass
class Player:
    yellow = 0
    red = 0
    blue = 0
    black = 0
    green = 0
    white = 0
    noble_number = 0
    cards = []

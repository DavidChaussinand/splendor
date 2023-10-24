import dataclasses

from model.Board import Board
from model.Player import Player


@dataclasses.dataclass
class Game:
    board: Board
    player_list: list[Player]

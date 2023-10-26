from engine.GameStart import GameStart
from engine.Query import Query
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from repository.GameRepositoryInMemory import GameRepositoryInMemory


class GameLayout:
    def __init__(self):
        self.game_repository = GameRepositoryInMemory()
        self.game_start = GameStart(self.game_repository)
        self.query = Query(self.game_repository)
        self.take_different_color_token = TakeDifferentColorToken(self.game_repository)
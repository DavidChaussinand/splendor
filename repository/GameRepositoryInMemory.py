import copy
import dataclasses

from model.Board import Board


class GameRepositoryInMemory:

    def get_game(self):
        return copy.deepcopy(self.game)

    def save_game(self, game):
        self.game = game

from model.Board import Board


class GameRepositoryInMemory:

    def get_game(self):
        return self.game

    def save_game(self, game):
        self.game = game

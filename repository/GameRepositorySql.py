from model import Game
from model import Player
from model import Board
from model import Stock

from webgame.models import *


class GameRepositorySql:
    def __init__(self):
        self.stock_board = StockDB.objects.create()
        self.stock_board.save()
        self.stock_player = StockDB.objects.create()
        self.stock_player.save()
        self.board = BoardDB.objects.create(self.stock_board)
        self.board.save()
        self.game = GameDB.objects.create(self.board)
        self.game.save()
        self.player = PlayerDB.objects.create(self.stock_player, self.game)
        self.player.save()

    def save_game(self, game_state):
        self.game.board.stock.red = game_state.board.stock.red
        self.game.save()
        self.player.stock.red = game_state.player_list[0].stock.red
        self.player.save()

    # def get_game(self):
    #     game.board.stock.red = self.game.board.stock.red
    #     game.player_list.player[0].stock.red = self.player.stock.red

from model.Game import Game
from model.Player import Player
from model.Board import Board
from model.Stock import Stock

from webgame import models as db


class GameRepositorySql:
    def __init__(self):
        self.stock_board = db.Stock.objects.create()
        self.stock_player = db.Stock.objects.create()
        self.board = db.Board.objects.create(stock=self.stock_board)
        self.game = db.Game.objects.create(board=self.board)
        self.player = db.Player.objects.create(stock=self.stock_player, game=self.game)

    def save_game(self, game):
        self.game.board.stock.red = game.board.stock.red
        self.game.save()
        self.player.stock.red = game.player_list[0].stock.red
        self.player.save()

    def get_game(self):
        board = Board(yellow=0, stock=Stock(0, 0, 0, 0, 0),
                      noble_number=0, card_level1=0, card_level2=0,
                      card_level3=0,
                      cards=[])

        player0 = Player(yellow=0, stock=Stock(0, 0, 0, 0, 0), noble_number=0, cards=[], cards_reserved=[])

        game = Game(board, player_list=[player0])

        game.board.stock.red = self.game.board.stock.red
        game.player_list[0].stock.red = self.player.stock.red

        return game

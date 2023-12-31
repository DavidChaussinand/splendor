from model.Board import Board
from model.Game import Game
from model.Player import Player
from model.Stock import Stock


class GameStart:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_player):
        if number_of_player > 4:
            raise (TooManyPlayersException)
        noble_number = number_of_player + 1
        if number_of_player == 2:
            token_number = 4
        elif number_of_player == 3:
            token_number = 5
        elif number_of_player == 4:
            token_number = 7
        player_list = []
        for x in range(number_of_player):
            player = Player(yellow=0,stock=Stock(0,0,0,0,0),noble_number=0,cards=[],cards_reserved=[])
            player_list.append(player)

        board = Board(yellow=5, stock=Stock(token_number, token_number, token_number, token_number, token_number), noble_number=noble_number, card_level1=4, card_level2=4,
                      card_level3=4,
                      cards=[])
        game = Game(board, player_list)
        self.game_repository.save_game(game)


class TooManyPlayersException (Exception):
    pass

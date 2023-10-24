from pprint import pprint

from model.Board import Board
from model.Player import Player


class GameStart:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_player):
        noble_number = number_of_player + 1
        if number_of_player == 2:
            token_number = 4
        elif number_of_player == 3:
            token_number = 5
        elif number_of_player == 4:
            token_number = 7
        player_list = []
        for x in range(number_of_player):
            player = Player()
            player_list.append(player)

        game_state = [Board(yellow=5, red=token_number, green=token_number, white=token_number, blue=token_number, black=token_number, noble_number=noble_number, card_level1=4, card_level2=4, card_level3=4),
                      player_list
        ]
        self.game_repository.save_game(game_state)

    def show_game_state(self):
        return self.game_repository.get_game()

from model.Board import Board


class GameStart:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_player):
        noble_number = number_of_player+1
        if number_of_player == 2:
            red = 4
        elif number_of_player == 3:
            red = 5
        elif number_of_player == 4:
            red = 7
        self.game_repository.save_game(Board(yellow=5, red=red, noble_number=noble_number, card_level1=4, card_level2=4, card_level3=4))
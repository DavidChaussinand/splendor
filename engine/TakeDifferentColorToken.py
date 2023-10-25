class TakeDifferentColorToken:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number):
        game = self.game_repository.get_game()
        game.player_list[player_number].red = 1
        game.player_list[player_number].green = 1
        game.player_list[player_number].black = 1
        self.game_repository.save_game(game)
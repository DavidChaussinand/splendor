class TakeDifferentColorToken:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number):
        game_state = self.game_repository.get_game()

        game_state[1][player_number].red=1
        game_state[1][player_number].black=1
        game_state[1][player_number].green=1


        self.game_repository.save_game(game_state)

        return game_state[1][player_number]


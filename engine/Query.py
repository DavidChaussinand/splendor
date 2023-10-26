class Query:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def show_game_state(self):
        return self.game_repository.get_game()

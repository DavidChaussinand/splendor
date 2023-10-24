class BuyCard:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number):
        game = self.game_repository.get_game()
        game.player_list[player_number].cards.append(game.board.card)
        game.board.card = None
        game.player_list[player_number].blue -= 3
        self.game_repository.save_game(game)

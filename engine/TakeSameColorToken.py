class TakeSameColorToken:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number, blue, green, red, black, white):
        game = self.game_repository.get_game()
        tokens = [("red", red), ("blue", blue), ("green", green), ("black", black), ("white", white), ]




        if game.board.stock.blue >= 4:
            for (color, taken) in tokens:
                if taken:
                    game.board.stock.decrease(color, quantity=2)
                    game.player_list[player_number].stock.increase(color, quantity=2)
        else:
            raise ValueError("pas assez de jeton dans le stock car inférieur à 4")

        self.game_repository.save_game(game)
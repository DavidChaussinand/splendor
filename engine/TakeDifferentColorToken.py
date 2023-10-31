class TakeDifferentColorToken:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number, blue, green, red, black, white):
        game = self.game_repository.get_game()
        tokens = [("red", red), ("blue", blue), ("green", green), ("black", black), ("white", white), ]
        counter = 0
        available_colors = 0
        for x in game.board.stock.__dict__:
            if game.board.stock.__dict__[x] > 0:
                available_colors += 1
        for (color, taken) in tokens:
            if taken:
                counter += 1
                game.board.stock.decrease(color, quantity=1)
                game.player_list[player_number].stock.increase(color, quantity=1)
        for x in game.board.stock.__dict__:
            if game.board.stock.__dict__[x] < 0:
                raise ValueError(f'No {x} tokens on board')
        if (counter < 3 and available_colors > counter) or counter > 3:
            raise ValueError('not right amount of token taken')
        self.game_repository.save_game(game)

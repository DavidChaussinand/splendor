from model.Card import Card


class BuyCard:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number, card_number):
        game = self.game_repository.get_game()
        card = game.board.cards[card_number]
        player = game.player_list[player_number]
        player.cards.append(card)
        del game.board.cards[card_number]

        for color in card.cost.__dict__:
            player.stock.decrease(color, card.cost.__dict__[color])
            game.board.stock.increase(color, card.cost.__dict__[color])

        for value in player.stock.__dict__.values():
            if value < 0:
                raise ValueError('Not enough tokens')

        self.game_repository.save_game(game)



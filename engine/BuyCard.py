from model.Card import Card


class BuyCard:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number, card_number):
        game = self.game_repository.get_game()
        card = game.board.cards[card_number]
        game.player_list[player_number].cards.append(card)
        del game.board.cards[card_number]

        for color in card.cost.__dict__:
            game.player_list[player_number].stock.decrease(color, card.cost.__dict__[color])

        enough_tokens = True
        for value in game.player_list[player_number].stock.__dict__.values():
            if value < 0:
                enough_tokens = False

        if enough_tokens:
            self.game_repository.save_game(game)
        else:
            raise ValueError('Not enough tokens')


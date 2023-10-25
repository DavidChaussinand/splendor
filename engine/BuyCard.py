from model.Card import Card


class BuyCard:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, player_number):
        game = self.game_repository.get_game()
        card = game.board.cards[0]
        game.player_list[player_number].cards.append(card)

        for color in card.cost:
            game.player_list[player_number].stock.decrease(color, card.cost[color])

        self.game_repository.save_game(game)

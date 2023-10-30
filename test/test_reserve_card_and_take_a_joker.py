import pytest

from engine.GameStart import GameStart
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from model.Board import Board
from model.Card import Card
from model.Cost import Cost
from model.Game import Game
from model.Player import Player
from model.Stock import Stock
from repository.GameRepositoryInMemory import GameRepositoryInMemory

class Card_reserved:

    def __init__(self,game_repository):
        self.game_repository= game_repository

    def execute(self, player_number, card_number):
        game = self.game_repository.get_game()
        card = game.board.cards[card_number]
        game.player_list[player_number].cards_reserved.append(card)
        del game.board.cards[card_number]
        self.game_repository.save_game(game)

@pytest.fixture
def game_repository():
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(3)
    return game_repository

def test_reserve_card(game_repository):
    # given
    # en tant que joueur je souhaite reserver la carte de mon choix.
    game = game_repository.get_game()
    card1 = Card(Cost(0, 3, 0, 0, 0))
    game.board.cards.append(card1)
    game_repository.save_game(game)
    card_reserved = Card_reserved(game_repository)
    # when
    # quand je reserve une carte .
    card_reserved.execute(2,0)
    game = game_repository.get_game()
    # then
    # j'ai une carte (problème du front: non visible ) dans mon deck
    actual = len(game.player_list[2].cards_reserved)
    expected = 1

    assert actual == expected



# def create_stock(quantity):
#     return Stock(quantity, quantity, quantity, quantity, quantity)
#
#
# class TakeYellowToken:
#
#     def __init__(self, game_repository):
#         self.game_repository = game_repository
#
#     def execute(self,player_number,joker):
#         joker = game_repository().get_game().board.yellow
#         game = self.game_repository.get_game()
#         game.board.stock.decrease(joker, quantity=1)
#         game.player_list[player_number].stock.increase(joker, quantity=1)
#         self.game_repository.save_game(game)


# def test_take_a_joker(game_repository):
#
#         player_number = 0
#         take_joker = TakeYellowToken(game_repository)
#         take_joker.execute(player_number, joker=True)
#         expected = (Game(Board(yellow=5,
#                                stock=Stock(red=4, green=3, black=4, white=3, blue=3),
#                                card_level1=4,
#                                card_level2=4,
#                                card_level3=4,
#                                noble_number=3,
#                                cards=[]),
#                          player_list=[
#                              Player(yellow=0, stock=Stock(0, 1, 1, 0, 1), noble_number=0, cards=[], cards_reserved=[]),
#                              Player(yellow=0, stock=Stock(0, 0, 0, 0, 0), noble_number=0, cards=[], cards_reserved=[])]),
#                     0,
#                     0,
#                     0,
#                     0,
#                     0)
#
#         actual = (game_repository.get_game(),
#                   game_repository.get_game().player_list[0].stock.blue,
#                   game_repository.get_game().player_list[0].stock.green,
#                   game_repository.get_game().player_list[0].stock.white,
#                   game_repository.get_game().player_list[0].stock.black,
#                   game_repository.get_game().player_list[0].stock.red)
#
#         assert actual == expected
#     # actual = stock.board yellow 5
#     # actual = stock player yellow 5
#     # expected = stock board yellow -1
#     # expected = stock player yellow -1
#     #
#     #
#     # et je prends un jeton joker qui est un jeton jaune.
#     # et j'enlève un jeton jaune du board
#     #assert actual == expected
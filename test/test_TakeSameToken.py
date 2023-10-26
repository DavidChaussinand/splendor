import pytest

from engine.GameStart import GameStart
from engine.TakeSameColorToken import TakeSameColorToken
from model.Board import Board
from model.Game import Game
from model.Player import Player
from model.Stock import Stock
from repository.GameRepositoryInMemory import GameRepositoryInMemory
@pytest.fixture
def game_repository():
    game_repository = GameRepositoryInMemory()
@pytest.fixture
def game_init(game_repository):
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(2)
    return game_repository


def create_stock(quantity):
    return Stock(quantity, quantity, quantity, quantity, quantity)

def test_take_same_color_token (game_init):
    player_number = 0
    game_repository = GameRepositoryInMemory()
    test_take_same_color_token = TakeSameColorToken(game_repository)
    game = Game(Board(yellow=5,
                      stock=Stock(red=4, green=4, black=4, white=4, blue=4),
                      card_level1=4,
                      card_level2=4,
                      card_level3=4,
                      noble_number=3,
                      cards=[]),
                player_list=[Player(yellow=0, stock=Stock(0, 0, 0, 0, 0), noble_number=0, cards=[]),
                             Player(yellow=0, stock=Stock(0, 0, 0, 0, 0), noble_number=0, cards=[])])
    game_repository.feed(game)
    test_take_same_color_token.execute(player_number, blue=True, green=False, white=False, black=False, red=False)
    actual = game_repository.get_game().board.stock.blue
    expected = 2
    assert actual == expected


def test_take_same_color_token_with_three_token_blue_on_the_board(game_repository):
    with pytest.raises(ValueError):
        player_number = 0
        game_repository = GameRepositoryInMemory()
        test_take_same_color_token = TakeSameColorToken(game_repository)
        game = Game(Board(yellow=5,
                               stock=Stock(red=4, green=4, black=4, white=4, blue=3),
                               card_level1=4,
                               card_level2=4,
                               card_level3=4,
                               noble_number=3,
                               cards=[]),
                         player_list=[Player(yellow=0,stock=Stock(0,0,0,0,0),noble_number=0,cards=[]), Player(yellow=0,stock=Stock(0,0,0,0,0),noble_number=0,cards=[])])

        # given
        # que le joueur n'a pas de jeton dans son stock

        game_repository.feed(game)

        # when
        # quand le joueur prend 2 jetons bleu
        test_take_same_color_token.execute(player_number, blue=True, green=False, white=False, black=False, red=False)

        # then
        # action impossible car pas assez de jetons dans le stock
        actual = game_repository.get_game().board.stock.blue
        expected = 3


        assert actual == expected

import pytest

from engine.GameStart import GameStart
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from model.Board import Board
from model.Game import Game
from model.Player import Player
from model.Stock import Stock
from repository.GameRepositoryInMemory import GameRepositoryInMemory

@pytest.fixture
def game_init():
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(2)
    return game_repository


def create_stock(quantity):
    return Stock(quantity, quantity, quantity, quantity, quantity)

def test_take_different_color_token (game_init):
    player_number = 0
    take_different_color_token = TakeDifferentColorToken(game_init)
    take_different_color_token.execute(player_number, blue=True, green=True, white=True, black=False, red=False)
    expected = (Game(Board(yellow=5,
                           stock=Stock(red=4, green=3, black=4, white=3, blue=3),
                           card_level1=4,
                           card_level2=4,
                           card_level3=4,
                           noble_number=3,
                           cards=[]),
                     player_list=[Player(yellow=0,stock=Stock(0,1,1,0,1),noble_number=0,cards=[],cards_reserved=[]), Player(yellow=0,stock=Stock(0,0,0,0,0),noble_number=0,cards=[],cards_reserved=[])]),
                1,
                1,
                1,
                0,
                0)

    actual = (game_init.get_game(),
              game_init.get_game().player_list[0].stock.blue,
              game_init.get_game().player_list[0].stock.green,
              game_init.get_game().player_list[0].stock.white,
              game_init.get_game().player_list[0].stock.black,
              game_init.get_game().player_list[0].stock.red)

    assert actual == expected
def test_take_token_from_empty_stock (game_init):
    with pytest.raises(ValueError):
        player_number = 0
        take_different_color_token = TakeDifferentColorToken(game_init)
        game = game_init.get_game()
        game.board.stock.green=0
        game_init.save_game(game)
        take_different_color_token.execute(player_number, blue=True, green=True, white=True, black=False, red=False)

def test_take_no_token (game_init):
    with pytest.raises(ValueError):
        player_number = 0
        take_different_color_token = TakeDifferentColorToken(game_init)
        take_different_color_token.execute(player_number, blue=False, green=False, white=False, black=False, red=False)

def test_take_to_many (game_init):
    with pytest.raises(ValueError):
        player_number = 0
        take_different_color_token = TakeDifferentColorToken(game_init)
        take_different_color_token.execute(player_number, blue=True, green=True, white=True, black=True, red=True)

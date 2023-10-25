import pytest

from engine.GameStart import GameStart
from model.Board import Board
from model.Stock import Stock
from model.Player import Player
from repository.GameRepositoryInMemory import GameRepositoryInMemory


@pytest.fixture
def game_repo():
    return GameRepositoryInMemory()


@pytest.fixture
def game_start(game_repo):
    return GameStart(game_repo)


def board_factory(number_of_player):
    noble_number = number_of_player + 1
    if number_of_player == 2:
        token_number = 4
    elif number_of_player == 3:
        token_number = 5
    else:
        token_number = 7

    return Board(yellow=5,
                 stock=Stock(token_number, token_number, token_number, token_number, token_number),
                 noble_number=noble_number,
                 card_level1=4,
                 card_level2=4,
                 card_level3=4,
                 cards=[])


@pytest.mark.parametrize("number_of_player,token_number,noble_number", [(2, 4, 3), (3, 5, 4), (4, 7, 5)])
def test_game_should_start(game_repo, game_start, number_of_player, token_number, noble_number):
    game_start.execute(number_of_player)
    actual = game_repo.get_game().board
    player_list = []
    for x in range(number_of_player):
        player = Player()
        player_list.append(player)

    expected = board_factory(number_of_player)
    assert actual == expected

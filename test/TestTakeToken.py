import pytest

from engine.GameStart import GameStart
from engine.TakeDifferentColorToken import TakeDifferentColorToken
from model.Player import Player
from repository.GameRepositoryInMemory import GameRepositoryInMemory

@pytest.fixture
def game_init():
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(3)
    return game_repository

def test_take_different_color_token (game_init):
    take_different_color_token = TakeDifferentColorToken(game_init)
    player = Player()
    player.red=1
    player.green=1
    player.black=1
    expected = player
    actual = take_different_color_token.execute(0)

    assert actual == expected
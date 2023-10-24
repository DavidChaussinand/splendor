import pytest

from engine.BuyCard import BuyCard
from engine.GameStart import GameStart
from repository.GameRepositoryInMemory import GameRepositoryInMemory


@pytest.fixture
def game_repository():
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(3)
    return game_repository


def test_buy_card(game_repository):
    buy_card = BuyCard(game_repository)
    buy_card.execute(2)
    game = game_repository.get_game()
    actual = game.player_list[2].cards
    expected = 1
    assert actual == expected


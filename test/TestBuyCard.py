import pytest

from engine.BuyCard import BuyCard
from engine.GameStart import GameStart
from model.Card import Card
from repository.GameRepositoryInMemory import GameRepositoryInMemory


@pytest.fixture
def game_repository():
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(3)
    return game_repository


def test_buy_free_card(game_repository):
    game = game_repository.get_game()
    card = Card()
    game.board.cards.append(card)
    game_repository.save_game(game)
    buy_card = BuyCard(game_repository)
    buy_card.execute(2)
    game = game_repository.get_game()
    actual = len(game.player_list[2].cards)
    expected = 1
    assert actual == expected


def test_buy_3blue_card(game_repository):
    game = game_repository.get_game()
    game.player_list[0].stock.increase("blue", 3)
    card = Card()
    card.cost["blue"] = 3
    game.board.cards.append(card)
    game_repository.save_game(game)
    buy_card = BuyCard(game_repository)
    buy_card.execute(0)
    expected = (3, 0)
    game_after = game_repository.get_game()
    actual = (game_after.player_list[0].cards[0].cost["blue"],
              game_after.player_list[0].stock.blue)
    assert actual == expected


def test_buy_3blue_1white_card(game_repository):
    game = game_repository.get_game()
    game.player_list[0].stock.increase("blue", 3)
    game.player_list[0].stock.increase("white", 3)
    card = Card()
    card.cost["blue"] = 3
    card.cost["white"] = 1
    game.board.cards.append(card)
    game_repository.save_game(game)
    buy_card = BuyCard(game_repository)
    buy_card.execute(0)
    expected = (3, 1, 0, 2)
    game_after = game_repository.get_game()
    actual = (game_after.player_list[0].cards[0].cost["blue"],
              game_after.player_list[0].cards[0].cost["white"],
              game_after.player_list[0].stock.blue,
              game_after.player_list[0].stock.white)
    assert actual == expected

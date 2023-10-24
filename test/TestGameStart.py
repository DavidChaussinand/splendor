from engine.GameStart import GameStart
from model.Board import Board
from repository.GameRepositoryInMemory import GameRepositoryInMemory





def game_should_start(number_of_player):
    game_repository = GameRepositoryInMemory()
    game_start = GameStart(game_repository)
    game_start.execute(number_of_player)
    return game_repository.get_game()


def test_game_should_start_1():
    actual = game_should_start(2)
    expected = Board(yellow=5, red=4, noble_number=3, card_level1=4, card_level2=4, card_level3=4)
    assert actual == expected


def test_game_should_start_3():
    actual = game_should_start(3)
    expected = Board(yellow=5, red=5, noble_number=4, card_level1=4, card_level2=4, card_level3=4)
    assert actual == expected

def test_game_should_start_4():
    actual = game_should_start(4)
    expected = Board(yellow=5, red=7, noble_number=5, card_level1=4, card_level2=4, card_level3=4)
    assert actual == expected

from engine.GameStart import GameStart
from model.Board import Board
from repository.GameRepositoryInMemory import GameRepositoryInMemory
from model.Stock import Stock



def test_show_game_state():
    repository = GameRepositoryInMemory()
    game_start = GameStart(repository)
    game_start.execute(2)
    expected = Board(yellow=5, stock=Stock(4, 4, 4, 4, 4), noble_number=3, card_level1=4, card_level2=4, card_level3=4, cards=[])
    actual = game_start.show_game_state().board
    assert actual == expected


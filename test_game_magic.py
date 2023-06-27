import random
import pytest
from game_of_loto_magic import Game

def test_game_str():
    game = Game()
    assert str(game) == "Game: player_score=0, comp_score=0"

def test_game_eq():
    game1 = Game()
    game2 = Game()
    assert game1 == game2

    game1.player_score = 1
    assert game1 != game2

def test_game_build_bingo_card():
    game = Game()
    card = game.build_bingo_card()

    assert len(card) == 3
    assert all(len(row) == 9 for row in card)

def test_game_mark_number():
    game = Game()
    card = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    marked_card = game.mark_number(card, 5)

    assert marked_card == [[1, 2, 3], [4, '-', 6], [7, 8, 9]]

def test_game_check_win():
    game = Game()

    # Test player win
    game.player_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    assert game.check_win() is True
    assert game.player_score == 1

    # Test computer win
    game.player_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game.comp_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    assert game.check_win() is True
    assert game.comp_score == 1

    # Test no win
    game.player_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game.comp_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    assert game.check_win() is False

# Add more tests if needed

if __name__ == "__main__":
    pytest.main()

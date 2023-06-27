from game_of_loto import Game
from unittest.mock import patch
import random

def test_build_bingo_card():
    game = Game()
    card = game.build_bingo_card()

    # Проверяем размер карточки
    assert len(card) == 3
    assert len(card[0]) == 9
    assert len(card[1]) == 9
    assert len(card[2]) == 9

    # Проверяем, что все ячейки на карточке заполнены числами или пустыми значениями
    for row in card:
        for cell in row:
            assert isinstance(cell, int) or cell == ''

def test_mark_number():
    game = Game()
    card = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    marked_card = game.mark_number(card, 5)

    # Проверяем, что число 5 заменено на "-"
    assert marked_card == [[1, 2, 3], [4, '-', 6], [7, 8, 9]]

def test_check_win():
    game = Game()

    # Проверяем победу игрока
    game.player_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    assert game.check_win() == True

    # Проверяем победу компьютера
    game.player_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game.comp_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    assert game.check_win() == True

@patch('builtins.input', side_effect=['y'])
def test_make_move(mock_input, capsys):
    game = Game()
    game.tokens = 1
    game.current_number = 5
    game.player_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game.comp_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    game.make_move()

def test_start_game(capsys):
    game = Game()
    game.start_game()
    captured = capsys.readouterr()
    assert "Начало игры" in captured.out

def test_print_bingo_card(capsys):
    game = Game()
    card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game.print_bingo_card(card)
    captured = capsys.readouterr()
    assert "1 2 3" in captured.out
    assert "4 5 6" in captured.out
    assert "7 8 9" in captured.out

@patch('builtins.input', side_effect=['y'])
def test_make_move(mock_input, capsys):
    game = Game()
    game.tokens = 1
    game.current_number = 5
    game.player_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game.comp_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    game.make_move()

    # Тест на зачеркивание цифры (победа игрока)
    user_input = lambda _: 'y'
    game.input = user_input
    game.make_move()
    captured = capsys.readouterr()
    assert "Вы победили!" in captured.out

    # Тест на незачеркивание цифры (победа компьютера)
    game.player_card = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    game.comp_card = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    user_input = lambda _: 'n'
    game.input = user_input
    game.make_move()
    captured = capsys.readouterr()
    assert "Компьютер победил." in captured.out

def test_end_game(capsys):
    game = Game()
    game.end_game()
    captured = capsys.readouterr()
    assert "Программа завершена." in captured.out


# Запустить все тесты с помощью pytest
# pytest -v test_game.py


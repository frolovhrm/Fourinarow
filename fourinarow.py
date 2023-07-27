"""Four-in-a-Row, by Al Sweigart al@inventwithpython.com
 Игра на выстраивание четырех фишек в ряд."""

import sys

EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

# Примечание: если изменяете один параметр изменяйте и другие
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_HEIGHT

# Шаблонная строка для вывода игравого поля
BOFRD_TEMPLATE = """

    1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""

def main():
    print(
        """ Four-in-a-Row, by Al Sweigart al@inventwithpython.com 
        
        Два игрока по очереди опускают фишки в один из семи столбцов,
        стараясь выстроить четыре фишки по вертикали, горизонтали или диаганали.
        """
    )
    # Подготовка новой игры
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    
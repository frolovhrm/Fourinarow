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

    while True:
        # Вывод игрового поля и получение хода игрока:
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # проверка победы или ничьи:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # В последний раз вывести поле
            print("Player {} has won!".format(playerTurn))
            sys.exit

        elif isFull(gameBoard):
            displayBoard(gameBoard)  # В постедний раз вывести поле
            print("This is a tie!")
            sys.exit

        # Ход передается другому игроку
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X
def getNewBoard():
    """ Возвращает словарь, представляющий игровое поле.
    
    Ключи - кортежи(columnIndex, rowIndex) с двумя целыми числами,
    а значения - одна из строк 'X', 'O' или '.' (пробел). """
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

def displayBoard(board):
    """Выводит на экран игровое поле и фишки"""

    # Подготовить список, передаваемый строковому методу forman() для
    # шаблона игрового поля. Список содержит все фишки игрового поля
    # и пустые ячейки, перечисляемые слева направо, сверху вниз:
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])
    
    # Выводит игровое поле:
    print(BOFRD_TEMPLATE.format(*tileChars))

def getPlayerMove(playerTile, board):
    """ Предлогает игроку выбрать столбец для размещения фишки.
    
    Возвращает кортеж (столбец, строка) итогового положения фишки."""

    while True:
        print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} or QUIT:")
        response = input("> ").upper().strip()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit
            
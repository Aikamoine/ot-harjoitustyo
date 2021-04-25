from gamelogic.gameboard import Gameboard
from ui.gameloop import Gameloop
from repositories.sudoku_loader import SudokuLoader

def main():
    loader = SudokuLoader()
    board = Gameboard(loader)

    loop = Gameloop(board, 500)
    loop.start()

if __name__ == '__main__':
    main()

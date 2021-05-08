from initialize_database import initialize_database
from gamelogic.gameboard import Gameboard
from ui.gameloop import Gameloop
from repositories.sudoku_loader import SudokuLoader
from connections import get_database_connection
from connections import database_exists

def main():
    if not database_exists():
        initialize_database()
    loader = SudokuLoader(get_database_connection())
    board = Gameboard(loader)

    loop = Gameloop(board, 500)
    loop.start()
if __name__ == '__main__':
    main()

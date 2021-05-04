import math
from entities.tile import Tile
from gamelogic.game_logic import GameLogic

class Gameboard:
    """Contains the information for the whole sudoku
    Attributes:
        puzzle: two-dimensional array of Tiles
        solution: two-dimensional array of Tiles that contain correct answers
        board_length: length of the puzzle, regular sudoku is 9
        board_squared: the squared value the sudoku board's length, so 3 for a regular sudoku
        loader: SudokuLoader for getting a new puzzle
        logic: Gamelogic object for checking player moves contra the rules
    """
    def __init__(self, loader, row_length=9):
        """
        Args:
            loader (SudokuLoader): SudokuLoader for loading and saving sudokus
            row_length (int, optional): Length of the board's side. Defaults to 9.
        """
        self.puzzle = []
        self.solution = []
        self.board_length = row_length
        self.board_squared = int(math.sqrt(row_length))
        self.loader = loader
        self.logic = None

    def set_up_game(self, difficulty):
        """Sets up a new ready-to-play game state

        Args:
            difficulty (string): chosen game difficulty
        """
        self.loader.load_random_puzzle(difficulty)
        self.puzzle = self._set_tiles(self.loader.puzzle)
        self.solution = self._set_tiles(self.loader.solution)
        self.logic = GameLogic(self.puzzle)

    def load_saved_game(self):
        """Sets up the last saved game to be played.
           If no saved game exists, defaults to setting an easy sudoku 
        """
        if self.loader.load_saved_game():
            self.puzzle = self._set_tiles(self.loader.puzzle)
            self.solution = self._set_tiles(self.loader.solution)
            self.logic = GameLogic(self.puzzle)
        else:
            self.set_up_game("easy")
    
    def _set_tiles(self, sudoku):
        """Formats an array of integers into an array of Tiles.

        Args:
            sudoku (2-dimensional array of int): array representation of a sudoku

        Returns:
            [2-dimensional array of Tiles]: an array of Tiles
        """
        sudoku_array = []
        for row in range(self.board_length):
            column_array = []
            for column in range(self.board_length):
                tile = Tile(row, column)
                tile.value = sudoku[row][column]
                if tile.value > 0:
                    tile.initial = True
                column_array.append(tile)
            sudoku_array.append(column_array)
        return sudoku_array

    def add_value(self, row, column, value):
        """Adds a value to the sudoku, if move is legal and the Tile isn't part of original puzzle

        Args:
            row (int): row of the value to be changed
            column (int): column of the value to be changed
            value (int): value to be changed to

        Returns:
            [bool]: True if change is allowed, False otherwise
        """
        tile = self.puzzle[row][column]

        if not self.logic.can_add_value(tile, value):
            return False

        return tile.change_value(value)

    def add_correct_value(self, add_to_x, add_to_y):
        """Gets a value from the solution corresponding to the coordinates and adds it to board 

        Args:
            add_to_x (int): row of the value to be changed
            add_to_y (int): column of the value to be changed
        """
        return self.add_value(add_to_x, add_to_y,
                       self.solution[add_to_x][add_to_y].value)

    def remove_value(self, row, column):
        """Removes a value at coordinates, if it isn't part of the original puzzle

        Args:
            row (int): row of the value to be changed
            column (int): column of the value to be changed

        Returns:
            [bool]: True if deletion is succesful, False otherwise
        """
        tile = self.puzzle[row][column]
        return tile.change_value(0)

    def is_full(self):
        """Checks if the board is full, i.e. game is won

        Returns:
            [bool]: True if board is full, False otherwise
        """
        for row in range(self.board_length):
            for col in range(self.board_length):
                if self.puzzle[row][col].value == 0:
                    return False
        return True

    def save(self):
        """Saves the game state and solution
        """
        self.loader.save(self.puzzle, self.solution)

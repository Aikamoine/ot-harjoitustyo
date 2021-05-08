import random
import sqlite3
from repositories.sudoku_formatter import SudokuFormatter

class SudokuLoader:
    """Class for loading sudokus to and from a database. Holds currently loaded values.

    Attributes:
        formatter: SudokuFormatter for manipulating sudoku representations
        puzzle: currently loaded puzzle
        solution: currently loaded solution
        connection: database connection
        cursor: database cursor
    """
    def __init__(self, connection):
        """
        Args:
            connection (sqlite3 Connection): connection to database
        """
        self.formatter = SudokuFormatter()
        self.puzzle = []
        self.solution = []
        self.connection = connection
        self.cursor = self.connection.cursor()

    def load_random_puzzle(self, difficulty):
        """Loads a random puzzle and its solution

        Args:
            difficulty (string): difficulty to be loaded
        """
        sudokus = self.cursor.execute(
            '''SELECT puzzle, solution FROM sudokus WHERE difficulty=(?)''', (difficulty,))
        results = sudokus.fetchall()
        random_sudoku = results[random.randint(0, len(results) - 1)]

        self.puzzle = self.formatter.string_to_grid(random_sudoku[0])
        self.solution = self.formatter.string_to_grid(random_sudoku[1])

    def load_saved_game(self):
        """Loads a previously saved game, if one exists

        Returns:
            [bool]: True if saved game is found, False otherwise
        """
        sudokus = self.cursor.execute(
            '''SELECT puzzle, solution FROM savedgames WHERE savename=(?)''', ("lastsave",))
        results = sudokus.fetchall()
        if len(results) == 0:
            return False
        saved_sudoku = results[0]

        self.puzzle = self.formatter.string_to_grid(saved_sudoku[0])
        self.solution = self.formatter.string_to_grid(saved_sudoku[1])
        return True

    def save(self, puzzle, solution):
        """Saves the given puzzle and solution

        Args:
            puzzle (2-dimensional array of Tiles): current state of the puzzle
            solution (2-dimensional array of Tiles): solution to the puzzle

        Returns:
            [bool]: True if save is succesful, False othewise
        """
        puzzle_string = self.formatter.grid_to_string(puzzle)
        solution_string = self.formatter.grid_to_string(solution)

        try:
            self.cursor.execute(
                                '''REPLACE INTO savedgames VALUES(?,?,?)''',
                                ("lastsave", puzzle_string, solution_string))
            self.connection.commit()
            return True
        except sqlite3.OperationalError:
            return False

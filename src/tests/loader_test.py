import unittest
import sqlite3
import os
from entities.tile import Tile
from repositories.sudoku_loader import SudokuLoader
from initialize_database import drop_tables
from initialize_database import create_tables
from initialize_database import add_to_database

class TestLoader(unittest.TestCase):
    """Class for testing database select and add operations

    Attributes:
        database_path: location of the test database
        connection: sqlite3 connection
    """

    def setUp(self):
        """Creates a database that is equal to the actual program. 
           Inserts one test sudoku to the database.
        """
        self.database_path = 'src//tests//test_database.db'
        self.connection = sqlite3.connect(self.database_path)
        drop_tables(self.connection, self.connection.cursor())
        create_tables(self.connection, self.connection.cursor())

        sudokudata = self._get_test_sudoku_data()
        add_to_database(sudokudata, self.connection, self.connection.cursor())

        self.loader = SudokuLoader(self.connection)

    def _get_test_sudoku_data(self):
        """
        Returns:
            [Array of string]: Test sudoku. Contains puzzle, solution and difficulty
        """
        data = ["001309000200000003000180490060000007003000046742000000000041080970000000008070600",
                "451369872289754163637182495165498237893217546742635918326541789974826351518973624",
                "medium"] 
        return data

    def _remove_test_database(self):
        """Deletes the test database file
        """
        if os.path.exists(self.database_path):
            os.remove(self.database_path)

    def _get_test_puzzle(self):
        """Returns the test puzzle in a 2-dimensional array format

        Returns:
            [2-dimensional array of int]: test puzzle in a 2-dimensional array format
        """
        puzzle = [
                  [0,0,1,3,0,9,0,0,0],[2,0,0,0,0,0,0,0,3],[0,0,0,1,8,0,4,9,0],
                  [0,6,0,0,0,0,0,0,7],[0,0,3,0,0,0,0,4,6],[7,4,2,0,0,0,0,0,0],
                  [0,0,0,0,4,1,0,8,0],[9,7,0,0,0,0,0,0,0],[0,0,8,0,7,0,6,0,0]
                 ]
        return puzzle

    def _get_test_solution(self):
        """Returns the test solution in a 2-dimensional array format

        Returns:
            [2-dimensional array of int]: test soluton in a 2-dimensional array format
        """
        solution = [
                    [4,5,1,3,6,9,8,7,2],[2,8,9,7,5,4,1,6,3],[6,3,7,1,8,2,4,9,5],
                    [1,6,5,4,9,8,2,3,7],[8,9,3,2,1,7,5,4,6],[7,4,2,6,3,5,9,1,8],
                    [3,2,6,5,4,1,7,8,9],[9,7,4,8,2,6,3,5,1],[5,1,8,9,7,3,6,2,4]
                   ]
        return solution

    def _int_array_to_tile_array(self, int_grid):
        """[summary]

        Args:
            int_grid (2-dimensional array of int): Sudoku grid with int values

        Returns:
            [2-dimensional array of Tile]: Sudoku grid with Tile objects
        """
        tile_grid = []
        for row in range(0, 9):
            row_array = []
            for col in range(0, 9):
                tile = Tile(row, col)
                tile.value = int_grid[row][col]
                row_array.append(tile)
            tile_grid.append(row_array)
        return tile_grid

    def test_load_random_puzzle_loads_correctly(self):
        self.loader.load_random_puzzle("medium")

        correct_puzzle = self._get_test_puzzle()
        correct_solution = self._get_test_solution()

        self.assertEqual(self.loader.puzzle, correct_puzzle)
        self.assertEqual(self.loader.solution, correct_solution)

        self._remove_test_database()

    def test_save_game_returns_true_on_empty_database(self):
        save_puzzle = self._int_array_to_tile_array(self._get_test_puzzle())
        save_solution = self._int_array_to_tile_array(self._get_test_solution())

        save_puzzle[0] = save_solution[0]
        save_puzzle[1] = save_solution[1]
        save_puzzle[2] = save_solution[2]

        self.assertEqual(self.loader.save(save_puzzle, save_solution), True)

        self._remove_test_database()

    def test_load_saved_game_returns_correct_game(self):
        save_puzzle = self._int_array_to_tile_array(self._get_test_puzzle())
        save_solution = self._int_array_to_tile_array(self._get_test_solution())

        save_puzzle[0] = save_solution[0]
        save_puzzle[1] = save_solution[1]
        save_puzzle[2] = save_solution[2]

        self.loader.save(save_puzzle, save_solution)
        self.loader.load_saved_game()

        for row in range(9):
            for col in range(9):               
                self.assertEqual(self.loader.puzzle[row][col], save_puzzle[row][col].value)
                self.assertEqual(self.loader.solution[row][col], save_solution[row][col].value)

        self._remove_test_database()

    def test_load_saved_game_returns_false_if_nothing_saved(self):
        self.assertEqual(self.loader.load_saved_game(), False)

        self._remove_test_database()

    def test_save_returns_false_is_table_does_not_exist(self):
        drop_tables(self.connection, self.connection.cursor())
        
        save_puzzle = self._int_array_to_tile_array(self._get_test_puzzle())
        save_solution = self._int_array_to_tile_array(self._get_test_solution())

        save_puzzle[0] = save_solution[0]
        save_puzzle[1] = save_solution[1]
        save_puzzle[2] = save_solution[2]

        self.assertEqual(self.loader.save(save_puzzle, save_solution), False)
        
        self._remove_test_database()

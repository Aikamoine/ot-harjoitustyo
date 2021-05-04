import unittest
from repositories.sudoku_formatter import SudokuFormatter
from entities.tile import Tile

class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = SudokuFormatter()
        self.string = "267389154394516872851427693549000000726000000138000000475938261682145937913762548"
        self.grid = []
        self.grid.append([2, 6, 7, 3, 8, 9, 1, 5, 4])
        self.grid.append([3, 9, 4, 5, 1, 6, 8, 7, 2])
        self.grid.append([8, 5, 1, 4, 2, 7, 6, 9, 3])
        self.grid.append([5, 4, 9, 0, 0, 0, 0, 0, 0])
        self.grid.append([7, 2, 6, 0, 0, 0, 0, 0, 0])
        self.grid.append([1, 3, 8, 0, 0, 0, 0, 0, 0])
        self.grid.append([4, 7, 5, 9, 3, 8, 2, 6, 1])
        self.grid.append([6, 8, 2, 1, 4, 5, 9, 3, 7])
        self.grid.append([9, 1, 3, 7, 6, 2, 5, 4, 8])

    def test_string_to_grid_returns_correct_grid(self):
        self.assertEqual(self.formatter.string_to_grid(self.string), self.grid)

    def test_grid_to_string_returns_correct_string(self):
        tile_grid = []
        for row in range(0, 9):
            row_array = []
            for col in range(0, 9):
                tile = Tile(row, col)
                tile.value = self.grid[row][col]
                row_array.append(tile)
            tile_grid.append(row_array)

        self.assertEqual(self.formatter.grid_to_string(tile_grid), self.string)

    def test_dots_to_zeros_returns_correct_array(self):
        csv_output = ["..13.9...2.......3...18.49..6......7..3....46742..........41.8.97.........8.7.6..",
                      "451369872289754163637182495165498237893217546742635918326541789974826351518973624",
                      "medium"]
        formatted_array = self.formatter.dots_to_zeros(csv_output)
        self.assertEqual(formatted_array[0], "001309000200000003000180490060000007003000046742000000000041080970000000008070600")
        self.assertEqual(formatted_array[1], "451369872289754163637182495165498237893217546742635918326541789974826351518973624")
        self.assertEqual(formatted_array[2], "medium")

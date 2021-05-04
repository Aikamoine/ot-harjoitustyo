import math

class SudokuFormatter:
    """Class for handling changes in different representations of sudokus
    """
    def string_to_grid(self, sudoku_string):
        """Formats a string representation of sudoku into a two-dimensional array

        Args:
            sudoku_string (string): sudoku in a string format, row by row

        Returns:
            [2-dimensional array of int]: sudoku in an array format
        """
        row_length = int(math.sqrt(len(sudoku_string)))
        sudoku = []
        for row in range(row_length):
            column = []
            for col in range(row_length):
                column.append(int(sudoku_string[row * row_length + col]))
            sudoku.append(column)
        return sudoku

    def grid_to_string(self, sudoku_grid):
        """Formats an array representation of sudoku into a string

        Args:
            sudoku_grid (2-dimensional array of Tile): sudoku in gameplay format

        Returns:
            [string]: sudoku in a string format, row by row
        """
        sudoku_string = ""
        for row in sudoku_grid:
            for col in row:
                sudoku_string += str(col.value)

        return sudoku_string

    def dots_to_zeros(self, sudoku_raw):
        """Formats the original csv's dots to zeros

        Args:
            sudoku_raw (array of string): array containing puzzle, solution and difficulty.
            The puzzle has dots representing empty tiles

        Returns:
            [array of strings]: sudoku's puzzle, solution and difficulty
        """
        sudoku_data = []
        sudoku_data.append(sudoku_raw[0].replace(".", "0"))
        sudoku_data.append(sudoku_raw[1].replace(".", "0"))
        sudoku_data.append(sudoku_raw[2])
        return sudoku_data

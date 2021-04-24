#import random
import math

class SudokuFormatter:
    def __init__(self, sudoku_csv):
        sudoku_csv = sudoku_csv.replace(".","0")
        self.sudoku_split = sudoku_csv.split(",")

    def get_puzzle(self):
        return self._format_grid(self.sudoku_split[0])

    def get_solution(self):
        return self._format_grid(self.sudoku_split[1])

    def _format_grid(self, sudoku_string):
        row_length = int(math.sqrt(len(sudoku_string))) - 1
        sudoku = []
        for row in range(row_length):
            column = []
            for col in range(row_length):
                column.append(int(sudoku_string[row * row_length + col]))
            sudoku.append(column)
        return sudoku

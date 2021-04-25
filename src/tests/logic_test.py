import unittest
from gamelogic.gameboard import Gameboard

class FakeLoader:
    def __init__(self):
        self.puzzle = []
        self.puzzle.append([2, 6, 7, 3, 8, 9, 1, 5, 4])
        self.puzzle.append([3, 9, 4, 5, 1, 6, 8, 7, 2])
        self.puzzle.append([8, 5, 1, 4, 2, 7, 6, 9, 3])
        self.puzzle.append([5, 4, 9, 0, 0, 0, 0, 0, 0])
        self.puzzle.append([7, 2, 6, 0, 0, 0, 0, 0, 0])
        self.puzzle.append([1, 3, 8, 0, 0, 0, 0, 0, 0])
        self.puzzle.append([4, 7, 5, 9, 3, 8, 2, 6, 1])
        self.puzzle.append([6, 8, 2, 1, 4, 5, 9, 3, 7])
        self.puzzle.append([9, 1, 3, 7, 6, 2, 5, 4, 8])

    def easy_sudoku(self):
        return self.puzzle

class Test_logic(unittest.TestCase):
    def setUp(self):
        loader = FakeLoader()
        self.board = Gameboard(loader)
        self.board.set_up_game(1)

    def test_add_duplicate_to_row_returns_false(self):
        self.assertFalse(self.board.add_value(3, 4, 5))

    def test_add_duplicate_to_column_returns_false(self):
        self.assertFalse(self.board.add_value(3, 3, 1))

    def test_add_duplicate_to_square_returns_false(self):
        self.board.add_value(3, 3, 2)
        self.assertFalse(self.board.add_value(3, 5, 2))

    def test_add_approved_value_returns_true(self):
        self.assertTrue(self.board.add_value(3, 3, 2))

    def test_add_zero_returns_false(self):
        self.assertFalse(self.board.add_value(3,5, 0))

    def test_cannot_change_initial_value(self):
        self.assertFalse(self.board.add_value(3, 2, 8))

#def example_solving_inputs():
 #   inputs = []

  #  inputs.append([3, 3, 2])
  #  inputs.append([3, 4, 7])
  #  inputs.append([3, 5, 1])
  #  inputs.append([4, 3, 8])
  #  inputs.append([4, 4, 5])
  #  inputs.append([4, 5, 3])
  #  inputs.append([5, 3, 6])
  #  inputs.append([5, 4, 9])
  #  inputs.append([5, 5, 4])
  #  inputs.append([3, 6, 3])
  #  inputs.append([3, 7, 8])
  #  inputs.append([3, 8, 6])
  #  inputs.append([4, 6, 4])
  #  inputs.append([4, 7, 1])
  #  inputs.append([4, 8, 9])
  #  inputs.append([5, 6, 7])
  #  inputs.append([5, 7, 2])
  #  inputs.append([5, 8, 5])
  #  return inputs

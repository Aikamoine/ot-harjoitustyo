import unittest
from gamelogic.gameboard import Gameboard

class FakeLoader:
    def __init__(self):
        self.puzzle = []
        self.solution = []
        
    def load_random_puzzle(self, difficulty):
        self._load_test_puzzle()

    def _load_test_puzzle(self):
        self.puzzle.append([2, 6, 7, 3, 8, 9, 1, 5, 4])
        self.puzzle.append([3, 9, 4, 5, 1, 6, 8, 7, 2])
        self.puzzle.append([8, 5, 1, 4, 2, 7, 6, 9, 3])
        self.puzzle.append([5, 4, 9, 0, 0, 0, 0, 0, 0])
        self.puzzle.append([7, 2, 6, 0, 0, 0, 0, 0, 0])
        self.puzzle.append([1, 3, 8, 0, 0, 0, 0, 0, 0])
        self.puzzle.append([4, 7, 5, 9, 3, 8, 2, 6, 1])
        self.puzzle.append([6, 8, 2, 1, 4, 5, 9, 3, 7])
        self.puzzle.append([9, 1, 3, 7, 6, 2, 5, 4, 8])
        self.solution.append([2, 6, 7, 3, 8, 9, 1, 5, 4])
        self.solution.append([3, 9, 4, 5, 1, 6, 8, 7, 2])
        self.solution.append([8, 5, 1, 4, 2, 7, 6, 9, 3])
        self.solution.append([5, 4, 9, 2, 7, 1, 3, 8, 6])
        self.solution.append([7, 2, 6, 8, 5, 3, 4, 1, 9])
        self.solution.append([1, 3, 8, 6, 9, 4, 7, 2, 5])
        self.solution.append([4, 7, 5, 9, 3, 8, 2, 6, 1])
        self.solution.append([6, 8, 2, 1, 4, 5, 9, 3, 7])
        self.solution.append([9, 1, 3, 7, 6, 2, 5, 4, 8])

class Test_logic(unittest.TestCase):
    def setUp(self):
        loader = FakeLoader()
        self.board = Gameboard(loader)
        self.board.set_up_game("easy")

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

    def test_add_correct_value_adds_correct(self):
        self.board.add_correct_value(3, 3)
        self.assertEqual(self.board.puzzle[3][3].value, 2)

    def test_remove_value_removes_player_added_value(self):
        self.board.add_value(3, 3, 2)
        self.board.remove_value(3, 3)
        self.assertEqual(self.board.puzzle[3][3].value, 0)

    def test_remove_value_does_not_remove_initial_value(self):
        self.board.remove_value(2, 3)
        self.assertEqual(self.board.puzzle[2][3].value, 4)

    def test_is_full_returns_false_if_not_full(self):
        self.assertEqual(self.board.is_full(), False)

    def test_is_full_returns_true_if_full(self):
        for row in range(0, 9):
            for col in range(0, 9):
                self.board.add_correct_value(row, col)
        self.assertEqual(self.board.is_full(), True)

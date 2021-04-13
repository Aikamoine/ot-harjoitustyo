import unittest
from tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile(3,4)

    def test_tile_initialisation(self):
        self.assertEqual(self.tile.x, 3)
        self.assertEqual(self.tile.y, 4)
        self.assertEqual(self.tile.value, 0)

    def test_tile_value_change_works_on_empty_tile(self):
        self.assertTrue(self.tile.change_value(5))
        self.assertEqual(self.tile.value, 5)

    def test_tile_value_change_does_not_work_on_nonempty(self):
        self.tile.value = 5
        self.assertFalse(self.tile.change_value(2))
        self.assertEqual(self.tile.value, 5)
    
    def test_tile_string_returns_expected_value(self):
        self.assertEqual(str(self.tile), "0")
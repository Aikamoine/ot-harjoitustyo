import math
from entities.tile import Tile
from gamelogic.game_logic import GameLogic

class Gameboard:
    def __init__(self, loader, row_length=9):
        self.tiles = []
        self.solution = []
        self.board_length = row_length
        self.board_square = int(math.sqrt(row_length))
        self.filled_tiles = 0
        self.is_full = False
        self.loader = loader

        for row in range(0, self.board_length):
            column_array = []
            for column in range(0, self.board_length):
                tile = Tile(row, column)
                column_array.append(tile)
            self.tiles.append(column_array)

        self.logic = GameLogic(self.tiles)

    def set_up_game(self, difficulty):
        if difficulty == 1:
            puzzle = self.loader.easy_sudoku()
        if difficulty == 2:
            puzzle = self.loader.hard_sudoku()

        for row in range(0, self.board_length):
            for column in range(0, self.board_length):
                tile = self.tiles[row][column]
                tile.value = puzzle[row][column]
                if tile.value > 0:
                    tile.initial = True
                    self.filled_tiles += 1

    def add_value(self, row, column, value):
        tile = self.tiles[row][column]

        if not self.logic.can_add_value(tile, value):
            return False
        if tile.change_value(value):
            self.filled_tiles += 1
            if self.filled_tiles == self.board_length * self.board_length:
                self.is_full = True
            return True
        return False

    def remove_value(self, row, column):
        tile = self.tiles[row][column]
        if not tile.change_value(0):
            return False
        self.filled_tiles -= 1
        return True

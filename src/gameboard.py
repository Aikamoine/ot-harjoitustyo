import math
from entities.tile import Tile
from game_logic import GameLogic

class Gameboard:
    def __init__(self, row_length):
        self.tiles = []
        self.board_length = row_length
        self.board_square = int(math.sqrt(row_length))
        self.filled_tiles = 0

        for row in range(0, self.board_length):
            column_array = []
            for column in range(0, self.board_length):
                tile = Tile(row, column)
                column_array.append(tile)
            self.tiles.append(column_array)

        self.logic = GameLogic(self.tiles)

    def print_board(self):
        for row in range(0, self.board_length):
            row_string = ""
            for column in range(0, self.board_length):
                tile = self.tiles[row][column]
                if tile.value == 0:
                    row_string = row_string + "  "
                else:
                    row_string = row_string + str(tile) + " "
            print(row_string)

    def set_up_game(self, tiles):
        for row in range(0, self.board_length):
            for column in range(0, self.board_length):
                tile = self.tiles[row][column]
                tile.value = tiles[row][column]
                if tile.value > 0:
                    tile.initial = True
                    self.filled_tiles += 1

    def add_value(self, row, column, value):
        tile = self.tiles[row][column]
        
        if not self.logic.can_add_value(tile, value):
            return False
        if tile.change_value(value):
            self.filled_tiles += 1
            return True
        return False

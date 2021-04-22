import math

class GameLogic:
    def __init__(self, tiles):
        self.tiles = tiles
        self.board_square = int(math.sqrt(len(tiles)))

    def can_add_value(self, tile, value):
        if value < 1 or value > len(self.tiles):
            return False
        if not self.can_add_to_square(tile, value):
            return False
        if not self.can_add_to_row(tile, value):
            return False
        if not self.can_add_to_column(tile, value):
            return False
        return True

    def can_add_to_square(self, tile, value):
        start_row = tile.row // self.board_square * self.board_square
        start_col = tile.column // self.board_square * self.board_square

        for row in range(start_row, start_row + self.board_square):
            for col in range(start_col, start_col + self.board_square):
                if self.tiles[row][col].value == value:
                    return False

        return True

    def can_add_to_row(self, tile, value):
        for column in range(0, len(self.tiles)):
            if self.tiles[tile.row][column].value == value:
                return False
        return True

    def can_add_to_column(self, tile, value):
        for row in range(0, len(self.tiles)):
            if self.tiles[row][tile.column].value == value:
                return False
        return True

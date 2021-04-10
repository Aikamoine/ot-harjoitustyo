from tile import Tile

class Gameboard:
    def __init__(self, row_length):
        self.tiles = []
        self.board_length = row_length * row_length
        for x in range(1, self.board_length + 1):
            column = []
            for y in range(1, self.board_length + 1):
                tile = Tile(x,y)
                column.append(tile)
            self.tiles.append(column)

    def print_board(self):
        for x in range(0, self.board_length):
            row = ""
            for y in range(0, self.board_length):
                tile = self.tiles[x][y]
                if tile.value == 0:
                    row = row + "  "
                else:
                    row = row + str(tile) + " "
            print(row)

    def set_up_game(self, tiles):
        for x in range(0, self.board_length):
            for y in range(0, self.board_length):
                self.tiles[x][y].value = tiles[x][y]

    def add_value(self, commands):
        cmds = commands.split(",")
        tile = self.tiles[int(cmds[0])][int(cmds[1])]
        return tile.change_value(cmds[2])
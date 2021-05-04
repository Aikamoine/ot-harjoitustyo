import math

class GameLogic:
    """Contains the rules of the game for changing values

    Attributes:
        puzzle: two-dimensional array with the sudoku's Tiles
        board_squared: the squared value the sudoku board's length, so 3 for a regular sudoku
    """
    def __init__(self, puzzle):
        """
        Args:
            puzzle (2-dimensional array of Tiles): the sudoku's puzzle
        """
        self.puzzle = puzzle
        self.board_squared = int(math.sqrt(len(puzzle)))

    def can_add_value(self, tile, value):
        """Checks if the change of the value is a legal move

        Args:
            tile (Tile): Tile to be changed
            value (int): value to be changed to

        Returns:
            [bool]: True, if value can be added, False otherwise
        """
        if value < 1 or value > len(self.puzzle):
            return False
        if not self.can_add_to_square(tile, value):
            return False
        if not self.can_add_to_row(tile, value):
            return False
        if not self.can_add_to_column(tile, value):
            return False
        return True

    def can_add_to_square(self, tile, value):
        """Checks if the change can be applied to its own square (3x3 in a regular sudoku)

        Args:
            tile (Tile): Tile to be changed
            value (int): value to be changed to

        Returns:
            [bool]: True, if value can be added, False otherwise
        """
        start_row = tile.row // self.board_squared * self.board_squared
        start_col = tile.column // self.board_squared * self.board_squared

        for row in range(start_row, start_row + self.board_squared):
            for col in range(start_col, start_col + self.board_squared):
                if self.puzzle[row][col].value == value:
                    return False

        return True

    def can_add_to_row(self, tile, value):
        """Checks if the change can be applied to its row

        Args:
            tile (Tile): Tile to be changed
            value (int): value to be changed to

        Returns:
            [bool]: True, if value can be added, False otherwise
        """
        for column in range(0, len(self.puzzle)):
            if self.puzzle[tile.row][column].value == value:
                return False
        return True

    def can_add_to_column(self, tile, value):
        """Checks if the change can be applied to its column

        Args:
            tile (Tile): Tile to be changed
            value (int): value to be changed to

        Returns:
            [bool]: True, if value can be added, False otherwise
        """
        for row in range(0, len(self.puzzle)):
            if self.puzzle[row][tile.column].value == value:
                return False
        return True

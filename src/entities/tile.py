class Tile:
    """The most atomic sudoku-unit.
       Contains information for one number or empty square

    Attributes:
        row: position on the sudoku board
        column: position on the sudoku board
        value: Tile's value
        initial: boolean, is tile a part of puzzles given numbers
    """
    def __init__(self, row, column):
        """
        Args:
            row (int): Tile's row on the sudoku board
            column (int): Tile's column on the sudoku board
        """
        self.row = row
        self.column = column
        self.value = 0
        self.initial = False

    def __str__(self):
        """
        Returns:
            [string]: Tile's value
        """
        if self.value == 0:
            return ""
        return str(self.value)

    def change_value(self, new_value):
        """changes the Tile's value, if the Tile is not a part of the original puzzle

        Args:
            new_value (int): value to be inserted

        Returns:
            [bool]: True, if value is updated, False otherwise
        """
        if self.initial:
            return False
        self.value = new_value
        return True

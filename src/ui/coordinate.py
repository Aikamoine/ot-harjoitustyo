class Coordinate:
    """Contains the value for an axis on the user interface
    Attributes:
        max_value: the greatest value on the board allowed, the size of the ui-board
        value: the current coordinate, initiates at 0
    """
    def __init__(self, max_value):
        """
        Args:
            max_value (Integer): the greatest value on the board allowed, the size of the ui-board
        """
        self.max_value = max_value
        self.value = 0

    def change_value(self, value):
        """moves the coordinate

        Args:
            value (double): changes the Coordinate, if the value wouldn't be too low or large
        """
        if self.value + value >= 0 and self.value + value < self.max_value - 1:
            self.value += value

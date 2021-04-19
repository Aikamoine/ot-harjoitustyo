class Tile:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = 0
        self.initial = False

    def __str__(self):
        return str(self.value)

    def change_value(self, new_value):
        if self.value != 0 and self.initial:
            return False
        self.value = new_value
        return True

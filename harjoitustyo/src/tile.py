class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0

    def __str__(self):
        return str(self.value)

    def change_value(self, new_value):
        if self.value == 0:
            self.value = new_value
            return True
        return False
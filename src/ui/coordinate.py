class Coordinate:
    def __init__(self, max_value):
        self.max_value = max_value
        self.value = 0

    def change_value(self, value):
        if self.value + value > 0 and self.value + value < self.max_value:
            self.value += value

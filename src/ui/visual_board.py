import pygame
from ui.coordinate import Coordinate

class VisualBoard:
    """Class that draws the game board for the player

    Attributes:
        board: Gameboard object containing the sudoku's data
        game_size: length of the drawn play area's side in pixels
        tile_size: length of one sudokus numbers' area in pixels
        display: pygame Display object for drawing the board
        font: pygame Font for writing the numbers
        selection_x: current selection's x axis on the board
        selection_y: current selection's x axis on the board
    """
    def __init__(self, board, game_size):
        """
        Args:
            board (Gameboard): Gameboard object containing the sudoku's data
            game_size (int): length of the drawn play area's side in pixels
        """
        self.board = board
        self.game_size = game_size
        self.tile_size = self.game_size / self.board.board_length
        pygame.init()
        self.display = pygame.display.set_mode(
            (self.game_size, self.game_size))
        self.font = pygame.font.SysFont(None, 40)
        self.selection_x = Coordinate(self.game_size)
        self.selection_y = Coordinate(self.game_size)

    def draw_board(self):
        """Draws the numbers from Gameboard
        """
        self.display.fill((255, 255, 255))
        for row in range(self.board.board_length):
            for col in range(self.board.board_length):
                tile = self.board.puzzle[row][col]

                text = self.font.render(str(tile), 1, (0, 0, 0))
                textpos = text.get_rect()
                textpos.x = col * self.tile_size + 20
                textpos.y = row * self.tile_size + 15

                self.display.blit(text, textpos)

        self.draw_grid_lines()
        self.highlight_selection()
        pygame.display.update()

    def draw_grid_lines(self):
        """Draws the sudokus grid around the numbers
        """
        for row in range(1, self.board.board_length):
            if row % self.board.board_squared == 0:
                thickness = 6
            else:
                thickness = 1
            pygame.draw.line(self.display, (0, 0, 0), (0, row * self.tile_size),
                            (self.game_size, row * self.tile_size), thickness)
            pygame.draw.line(self.display, (0, 0, 0), (row * self.tile_size, 0),
                            (row * self.tile_size, self.game_size), thickness)

    def move_selection(self, axis, direction):
        """
        Args:
            axis (string): which axis is to be moved
            direction (integer): which direction to move, negative is towards origo
        """
        if axis == "x":
            self.selection_x.change_value(direction * self.tile_size)
        if axis == "y":
            self.selection_y.change_value(direction * self.tile_size)

    def highlight_selection(self):
        thickness = 6
        start_x = self.selection_x.value
        start_y = self.selection_y.value
        end_x = self.selection_x.value + self.tile_size
        end_y = self.selection_y.value + self.tile_size

        pygame.draw.line(self.display, (0, 0, 0),
                        (start_x, start_y),
                        (end_x, start_y),
                        thickness)
        pygame.draw.line(self.display, (0, 0, 0),
                        (start_x, start_y),
                        (start_x, end_y),
                        thickness)
        pygame.draw.line(self.display, (0, 0, 0),
                        (end_x, start_y),
                        (end_x, end_y),
                        thickness)
        pygame.draw.line(self.display, (0, 0, 0),
                        (start_x, end_y),
                        (end_x, end_y),
                        thickness)

    def selection_to_cursor(self):
        mouse_coordinates = pygame.mouse.get_pos()
        self.selection_to_coordinates(mouse_coordinates[0], mouse_coordinates[1])

    def selection_to_coordinates(self, x_axis, y_axis):
        """Moves current selection to assigned coordinates.
           Converts the argument values to point at a Tiles top left
        Args:
            x_axis (float): value of x-axis
            y_axis (float): value of y-axis
        """
        self.selection_x.value = x_axis - (x_axis % self.tile_size)
        self.selection_y.value = y_axis - (y_axis % self.tile_size)

    def remove_value_at_selection(self):
        self.board.remove_value(int((self.selection_y.value + 1) // self.tile_size),
                               int((self.selection_x.value + 1) // self.tile_size))

    def add_value_at_selection(self, value):
        self.board.add_value(int((self.selection_y.value + 1) // self.tile_size),
                            int((self.selection_x.value + 1) // self.tile_size),
                            value)

    def add_correct_value(self):
        """Adds a correct value to current selection
        """
        add_to_x = int((self.selection_y.value + 1) // self.tile_size)
        add_to_y = int((self.selection_x.value + 1) // self.tile_size)
        self.board.add_correct_value(add_to_x, add_to_y)

    def save(self):
        """Saves game state
        """
        self.board.save()

    def victory(self):
        """Checks if game is won, i.e. the board is full

        Returns:
            [bool]: True if gameboard is full, False otherwise
        """
        return self.board.is_full()

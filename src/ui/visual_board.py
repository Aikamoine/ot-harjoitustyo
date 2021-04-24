import pygame
from ui.coordinate import Coordinate
from ui.menu import Menu

class VisualBoard:
    def __init__(self, board, game_size):
        self.board = board
        self.game_size = game_size
        self.tile_size = self.game_size / self.board.board_length
        pygame.init()
        self.display = pygame.display.set_mode(
            (self.game_size, self.game_size))
        self.font = pygame.font.SysFont(None, 40)
        self.selection_x = Coordinate(self.game_size)
        self.selection_y = Coordinate(self.game_size)
        self.fps = pygame.time.Clock()
        self.menu = Menu(self.display)

    def draw_board(self):
        self.display.fill((255, 255, 255))
        for row in range(self.board.board_length):
            for col in range(self.board.board_length):
                tile = self.board.tiles[row][col]

                text = self.font.render(str(tile), 1, (0, 0, 0))
                textpos = text.get_rect()
                textpos.x = col * self.tile_size + 20
                textpos.y = row * self.tile_size + 15

                self.display.blit(text, textpos)

        self.draw_grid_lines()
        self.highlight_selection()
        pygame.display.update()

    def draw_grid_lines(self):
        for row in range(self.board.board_length):
            if row % self.board.board_square == 0:
                thickness = 6
            else:
                thickness = 1
            pygame.draw.line(self.display, (0, 0, 0), (0, row * self.tile_size),
                            (self.game_size, row * self.tile_size), thickness)
            pygame.draw.line(self.display, (0, 0, 0), (row * self.tile_size, 0),
                            (row * self.tile_size, self.game_size), thickness)

    def move_selection(self, axis, direction):
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
        self.selection_x.value = mouse_coordinates[0] - (mouse_coordinates[0] % self.tile_size)
        self.selection_y.value = mouse_coordinates[1] - (mouse_coordinates[1] % self.tile_size)

    def remove_value_at_selection(self):
        self.board.remove_value(int((self.selection_y.value + 1) // self.tile_size),
                               int((self.selection_x.value + 1) // self.tile_size))

    def add_value_at_selection(self, value):
        self.board.add_value(int((self.selection_y.value + 1) // self.tile_size),
                            int((self.selection_x.value + 1) // self.tile_size),
                            value)

    def victory(self):
        return self.board.is_full

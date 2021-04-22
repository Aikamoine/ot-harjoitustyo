import pygame
from ui.coordinate import Coordinate

class VisualBoard:
    def __init__(self, board):
        self.board = board
        self.game_size = 500
        self.tile_size = self.game_size / self.board.board_length
        pygame.init()
        self.display = pygame.display.set_mode(
            (self.game_size, self.game_size))
        self.font = pygame.font.SysFont(None, 40)
        self.selection_x = Coordinate(self.game_size)
        self.selection_y = Coordinate(self.game_size)
        self.fps = pygame.time.Clock()

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            self.fps.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            self.draw_board()

            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.selection_x.change_value(-1 * self.tile_size)
                if event.key == pygame.K_RIGHT:
                    self.selection_x.change_value(self.tile_size)
                if event.key == pygame.K_UP:
                    self.selection_y.change_value(-1 * self.tile_size)
                if event.key == pygame.K_DOWN:
                    self.selection_y.change_value(self.tile_size)
                if event.unicode.isnumeric():
                    self.board.add_value(int((self.selection_y.value + 1) // self.tile_size),
                                         int((self.selection_x.value + 1) // self.tile_size),
                                         int(event.unicode))
        return True

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

import pygame
from ui.menu import Menu
from ui.visual_board import VisualBoard

class Gameloop:
    def __init__(self, board, game_size):
        pygame.init()
        self.display = pygame.display.set_mode(
            (game_size, game_size))
        self.start_menu = Menu(self.display)
        self.board_ui = VisualBoard(board, game_size)
        self.fps = pygame.time.Clock()

    def start(self):
        self.start_menu.draw_main()
        self.start_menu.run_menu()

        while True:
            if self.handle_events() is False:
                break
            self.fps.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            self.board_ui.draw_board()

            if event.type == pygame.QUIT:
                return False

            if self.board_ui.victory():
                victorymenu = Menu(self.display)
                victorymenu.draw_victory()
                victorymenu.run_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.board_ui.move_selection("x", -1)
                if event.key == pygame.K_RIGHT:
                    self.board_ui.move_selection("x", 1)
                if event.key == pygame.K_UP:
                    self.board_ui.move_selection("y", -1)
                if event.key == pygame.K_DOWN:
                    self.board_ui.move_selection("y", 1)
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    self.board_ui.remove_value_at_selection()
                if event.unicode.isnumeric():
                    self.board_ui.add_value_at_selection(int(event.unicode))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.board_ui.selection_to_cursor()
                if event.button == 3:
                    self.start_menu.run_menu()

        return True

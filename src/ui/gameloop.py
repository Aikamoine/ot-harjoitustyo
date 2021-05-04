import pygame
from ui.menu import MainMenu
from ui.menu import GameMenu
from ui.menu import WinMenu
from ui.visual_board import VisualBoard

class Gameloop:
    """Class that runs the pygame loop and communicates user actions to other classes

    Attributes:
        display: pygame Display object
        main_menu: main menu
        board = Gameboard object containing the sudokus data
        board_ui: VisualBoard object for drawing the gameboard
        fps: screen refresh rate
    """
    def __init__(self, board, game_size):
        """
        Args:
            board (Gameboard): Gameboard object containing the sudokus data
            game_size (float): game size in pixels
        """
        pygame.init()
        self.display = pygame.display.set_mode(
            (game_size, game_size))
        self.main_menu = MainMenu(self.display)
        self.board = board
        self.board_ui = VisualBoard(board, game_size)
        self.fps = pygame.time.Clock()

    def start(self):
        """Starts the game loop and runs until game is terminated
        """
        while True:
            if self.main_menu.initialize_new:
                self.initialize_game()

            if self._handle_events() is False:
                break
            self.fps.tick(60)
        pygame.quit()

    def initialize_game(self):
        """Gets settings from main menu to initialize a new game
        """
        self.main_menu.run_menu()
        if self.main_menu.load:
            self.board.load_saved_game()
            self.main_menu.load = False
        else:
            self.board.set_up_game(self.main_menu.difficulty)
        self.main_menu.initialize_new = False

    def _handle_events(self):
        """Listens to user actions during the game and forwards them to other classes

        Returns:
            [bool]: True if game is not over, False is game has been terminated
        """
        for event in pygame.event.get():
            self.board_ui.draw_board()

            if event.type == pygame.QUIT:
                return False

            if self.board_ui.victory():
                self._handle_victory()

            if event.type == pygame.KEYDOWN:
                self._handle_keydown(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mousedown(event)

        return True

    def _handle_keydown(self, event):
        """Handles a keyboard input

        Args:
            event (pygame Event): pygame Event
        """
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
        if event.key == pygame.K_ESCAPE:
            self._handle_pause()
        if event.unicode.isnumeric():
            self.board_ui.add_value_at_selection(int(event.unicode))

    def _handle_mousedown(self, event):
        """Handles mouse input

        Args:
            event (pygame Event): pygame Event
        """
        if event.button == 1:
            self.board_ui.selection_to_cursor()
        if event.button == 3:
            self.board_ui.selection_to_cursor()
            self._handle_pause()

    def _handle_pause(self):
        """Sets up mid-game menu. Menu functions are:
           - request a correct value from solution
           - save game state and return to main menu
        """
        game_menu = GameMenu(self.display)
        game_menu.run_menu()
        if game_menu.add_value:
            self.board_ui.add_correct_value()
        if game_menu.save_and_return:
            self.board_ui.save()
            self.main_menu.run_menu()

    def _handle_victory(self):
        """Sets up victory menu and returns to main menu if game is not terminated
        """
        victorymenu = WinMenu(self.display)
        victorymenu.run_menu()
        self.main_menu.run_menu()

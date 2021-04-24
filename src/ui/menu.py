import pygame_menu

class Menu:
    def __init__(self, display, difficulty=1):
        self.display = display
        display_x, display_y = display.get_size()
        self.menu = pygame_menu.Menu("Sudoku", display_x, display_y,
                                    theme=pygame_menu.themes.THEME_BLUE)
        self.difficulty = difficulty

    def draw_main(self):
        self.menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)],
                              onchange=self.change_difficulty)
        self.menu.add.button('Play', self.start_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def draw_victory(self):
        congratulation = "Voitit pelin. Toivottavasti olet ylpeä itsestäsi."
        self.menu.add.label(congratulation, max_char=-1)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def change_difficulty(self, value, difficulty):
        self.difficulty = difficulty

    def start_game(self):
        self.menu.disable()

    def run_menu(self):
        self.menu.enable()
        self.menu.mainloop(self.display)

import pygame_menu

class Menu:
    """Superclass for different menus
    Attributes:
        display: pygame Display
        menu: pygame_menu drawn on the display
    """
    def __init__(self, display):
        """
        Args:
            display (pygame Display): game area
        """
        self.display = display
        display_x, display_y = display.get_size()
        self.menu = pygame_menu.Menu("Sudoku", display_x, display_y,
                                    theme=pygame_menu.themes.THEME_BLUE)

    def close_menu(self):
        """Terminates the menu, allowing code execution to continue
        """
        self.menu.disable()

    def run_menu(self):
        self.menu.enable()
        self.menu.mainloop(self.display)

class MainMenu(Menu):
    """Main menu object
    Attributes:
        difficulty: currently selected difficulty
        load: flag for loading a previous game state
        initialize_new: flag for setting a new game state
    Args:
        Menu (Menu): superclass Menu
    """

    def  __init__(self, display):
        """
        Args:
            display (pygame Display): game area to draw on
        """
        super().__init__(display)
        self.difficulty = "easy"
        self.load = False
        self.initialize_new = True
        self.menu.add.selector('Vaikeusaste :', [('Heleppo', "easy"), ('Keskvaekee', "medium"),
                              ('Huastava', "hard"), ('Mahoton', "pro")],
                               onchange=self._change_difficulty)
        self.menu.add.button('Aloita', self.start)
        self.menu.add.button('Jatka edellistä', self._load_saved)
        self.menu.add.button('Lopeta', pygame_menu.events.EXIT)

    def _change_difficulty(self, value, difficulty):
        """Changes the difficulty flag.

        Args:
            value (string): difficulty name visible to user
            difficulty (string): difficulty name used in code
        """
        self.difficulty = difficulty
        self.initialize_new = True

    def start(self):
        self.initialize_new = True
        self.close_menu()

    def _load_saved(self):
        self.load = True
        self.initialize_new = True
        self.close_menu()

class GameMenu(Menu):
    """Menu object for mid-game
    Attributes:
        save_and_return: flag for saving game and returning to main menu
        add_value: flag for requesting correct value from solution
    Args:
        Menu (Menu): superclass Menu
    """
    def  __init__(self, display):
        """
        Args:
            display (pygame Display): game area to draw on
        """
        super().__init__(display)
        self.menu.add.button('Jatka', self.close_menu)
        self.menu.add.button('Anna oikea numero', self._add_correct_value)
        self.menu.add.button('Tallenna ja palaa päävalikkoon', self._return_to_main)
        self.menu.add.button('Lopeta tallentamatta', pygame_menu.events.EXIT)
        self.save_and_return = False
        self.add_value = False

    def _return_to_main(self):
        self.save_and_return = True
        self.close_menu()
    
    def _add_correct_value(self):
        self.add_value = True
        self.close_menu()

class WinMenu(Menu):
    """Menu object for victory-state

    Args:
        Menu (Menu): superclass Menu
    """
    def  __init__(self, display):
        """
        Args:
            display (pygame Display): game area to draw on
        """
        super().__init__(display)
        self.menu.add.label("Voitit pelin.", max_char=-1)
        self.menu.add.label("Toivottavasti olet ylpeä itsestäsi.", max_char=-1)
        self.menu.add.button('Takaisin päävalikkoon', self.close_menu)
        self.menu.add.button('Lopeta', pygame_menu.events.EXIT)

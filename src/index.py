#import pygame
from gameboard import Gameboard

def main():
    board = Gameboard(9)

    board.set_up_game(example_sudoku())
    #print("Pelataanko graafisella vai komentorivikäyttöliittymällä?")
    #print("Kirjoita pygame, jos haluat pelata graafisella käyttöliittymällä")

    #if input() == "pygame":
        #print("ei implementoitu")
        #height = board.board_length
        #width = height
        #display_height = height * 50
        #display_width = width * 50

        #display = pygame.display.set_mode((display_width, display_height))
        #pygame.display.set_caption("Sudoku")

        #pygame.init()
    #else:
    while True:
        print()
        board.print_board()

        move = input()
        if move == "end":
            break

        if move == "solve":
            for right_move in example_solving_inputs():
                board.add_value(
                    right_move[0], right_move[1], right_move[2])

        if board.filled_tiles == 9 * 9:
            board.print_board()
            print("Voitit pelin. Toivottavasti olet ylpeä itsestäsi...")
            break

        if len(move) == 5:
            commands = move.split(",")
            commands = list(map(int, commands))

            if not board.add_value(commands[0], commands[1], commands[2]):
                print("Arvoa ei voi lisätä tai muuttaa")


def example_sudoku():
    game = []

    game.append([2, 6, 7, 3, 8, 9, 1, 5, 4])
    game.append([3, 9, 4, 5, 1, 6, 8, 7, 2])
    game.append([8, 5, 1, 4, 2, 7, 6, 9, 3])
    game.append([5, 4, 9, 0, 0, 0, 0, 0, 0])
    game.append([7, 2, 6, 0, 0, 0, 0, 0, 0])
    game.append([1, 3, 8, 0, 0, 0, 0, 0, 0])
    game.append([4, 7, 5, 9, 3, 8, 2, 6, 1])
    game.append([6, 8, 2, 1, 4, 5, 9, 3, 7])
    game.append([9, 1, 3, 7, 6, 2, 5, 4, 8])

    return game

def example_solving_inputs():
    inputs = []

    inputs.append([3, 3, 2])
    inputs.append([3, 4, 7])
    inputs.append([3, 5, 1])
    inputs.append([4, 3, 8])
    inputs.append([4, 4, 5])
    inputs.append([4, 5, 3])
    inputs.append([5, 3, 6])
    inputs.append([5, 4, 9])
    inputs.append([5, 5, 4])
    inputs.append([3, 6, 3])
    inputs.append([3, 7, 8])
    inputs.append([3, 8, 6])
    inputs.append([4, 6, 4])
    inputs.append([4, 7, 1])
    inputs.append([4, 8, 9])
    inputs.append([5, 6, 7])
    inputs.append([5, 7, 2])
    inputs.append([5, 8, 5])
    return inputs

if __name__ == '__main__':
    main()

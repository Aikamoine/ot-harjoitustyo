from gameboard import Gameboard
from square import Square

def main():
    gb = Gameboard(3)
    game = []

    game.append([0,6,0,3,0,9,0,5,0])
    game.append([3,0,4,0,1,0,8,0,2])
    game.append([0,5,0,4,2,7,0,9,0])
    game.append([5,0,9,0,0,0,3,0,6])
    game.append([0,2,6,0,0,0,4,1,0])
    game.append([1,0,8,0,0,0,7,0,5])
    game.append([0,7,0,9,3,8,0,6,0])
    game.append([6,0,2,0,4,0,9,0,7])
    game.append([0,1,0,7,0,2,0,4,0])

    gb.set_up_game(game)
    print("Pelataan sudokua")

    while True:
        print()
        gb.print_board()

        move = input()
        if move == "end":
            break

        gb.add_value(move)

if __name__ == '__main__':
    main()
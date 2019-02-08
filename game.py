from board import Board
from menace import Menace
from random import randint

# TODO:
# 1)check if value given by the user is valid
# if it's not wrong


class Game:
    p1 = 9
    p2 = 8
    board = Board()
    menace = Menace()

    def __init__(self):
        print("game")

    def play(self):
        self.prepare_game()
        play = 1
        while play:
            play = self.move()
        if self.p1 < self.p2:
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    # values of P1 are 1's
    # values of P2 are 2's
    def move(self):
        if self.p1 > self.p2:
            print("Player 1 move")
            self.p1 -= 2
            pos = self.menace.move(self.board)
            print(pos)
            self.board.set_value_pos(pos, 1)
        else:
            print("Player 2 move")
            # pos = input("pos = ")
            pos = -1
            tmp = randint(1, self.p2)
            for i in range(0, 9):
                if self.board.get_board()[i] == 0:
                    if tmp == 1:
                        pos = i
                        break
                    else:
                        tmp -= 1
            if pos == -1:
                raise ValueError("Wrong Random")
            self.p2 -= 2
            self.board.set_value_pos(pos, 2)
        self.board.print_board()
        return self.board.check_winner_pos(pos)

    def prepare_game(self):
        self.board.clean()
        self.p1 = 9
        self.p2 = 8
        self.menace.clean()
        self.board.print_board()
        print(self.menace.__getattribute__('chosen'))
        print(self.menace.__getattribute__('last'))
        print(self.menace.__getattribute__('boxes'))


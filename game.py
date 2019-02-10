from board import Board
from menace import Menace
from random import randint
from player_random import Player_Random

# TODO:
# 1)check if value given by the user is valid
# if it's not wrong


class Game:
    p1 = 9
    p2 = 8
    board = Board()
    menace = Menace()
    player_random = Player_Random()

    # def __init__(self):
    #     print("game")

    def play(self):
        self.prepare_game()
        play = 1
        while self.p1 > 0 and play:
            score = self.move()
            if score == 0:
                if self.p1 < self.p2:
                    print("Player 1 wins")
                    self.menace.result(2)
                    return 1
                else:
                    print("Player 2 wins")
                    self.menace.result(0)
                    return 2
            elif score == -1:
                print("It's a draw")
                self.menace.result(1)
                return 0
            elif score == -2:
                print("Menace gave up")
                self.menace.result(0)
                return -1


    # values of P1 are 1's
    # values of P2 are 2's
    # return:
    # 0 - player 1 or player 2 win
    # 1 - no winner yet
    # -1 - draw
    def move(self):
        if self.p1 > self.p2:
            # print("Player 1 move")
            self.p1 -= 2
            pos = self.menace.move(self.board)
            if pos == -1:
                # self.board.print_board()
                return -1
            self.board.set_value_pos(pos, 1)
        else:
            # print("Player 2 move")
            # pos = input("pos = ")
            pos = self.player_random.move(self.p2, self.board.get_board())
            self.p2 -= 2
            self.board.set_value_pos(pos, 2)
        # self.board.print_board()
        return self.board.check_winner_pos(pos)

    def prepare_game(self):
        self.board.clean()
        self.p1 = 9
        self.p2 = 8
        self.menace.clean()
        # self.board.print_board()
        # print(self.menace.__getattribute__('chosen'))
        # print(self.menace.__getattribute__('last'))
        # print(self.menace.__getattribute__('boxes'))


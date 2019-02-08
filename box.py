from random import seed
from random import randint


class Box:
    # beads array:
    # -1 player 1 X
    # -2 player 2 O
    # 0 no beads in position
    beads = [0]*9

    # default number of beads for each option
    default = 1

    # number of colours, if box run out of one of the colour then decrease the number
    colours = 0

    # chosen in previous go
    chosen = -1

    # type = 0 for empty board
    # type != 0 for board with elements
    def __init__(self, box_type, board):
        seed(1000)
        if box_type == 0:
            self.beads = [3, 3, 0, 0, 3, 0, 0, 0, 0]
            self.colours = 3
        else:
            for i in range(0, 9):
                if board.get_board()[i] == 1:
                    self.beads[i] = -1
                elif board.get_board()[i] == 2:
                    self.beads[i] = -2
                else:
                    self.beads[i] = self.default
                    self.colours += 1

    # returns the place of the X/O that MENACE put
    # decreases the number of beads of the position
    # set the chosen value
    def move(self):
        tmp = randint(1, self.colours)
        for i in range(0, 9):
            if self.beads[i] > 0:
                if tmp == 1:
                    self.beads[i] -= 1
                    self.chosen = i
                    return i
                else:
                    tmp -= 1
        return -1

    # results:
    # 0 - lost
    # 1 - draw
    # 2 - win
    def result(self, result):
        if result == 1:
            self.beads[self.chosen] += 1
        elif result == 2:
            self.beads[self.chosen] += 3



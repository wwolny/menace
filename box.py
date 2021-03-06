from random import seed
from random import randint

# TODO:
# 1) write box to file
# 2) read box from file
# functions to use already "intelligent" boxes


class Box:
    # beads array:
    # -1 player 1 X
    # -2 player 2 O
    # 0 no beads in position

    # default number of beads for each option
    default = 1

    # number of colours, if box run out of one of the colour then decrease the number
    colours = 0

    # chosen in previous go
    chosen = -1

    # type = 0 for empty board
    # type != 0 for board with elements
    def __init__(self, box_type, board):
        self.beads = [0, 0, 0, 0, 0, 0, 0, 0, 0].copy()
        seed(1000)
        if box_type == 0:
            # self.beads = [3, 3, 0, 0, 3, 0, 0, 0, 0]
            self.beads[0] = 3
            self.beads[1] = 3
            self.beads[4] = 3
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
        # print(self.beads)
        tmp = randint(1, self.colours)
        for i in range(0, 9):
            if self.beads[i] > 0:
                if tmp == 1:
                    self.beads[i] -= 1
                    self.chosen = i
                    if self.beads[i] == 0:
                        self.colours -= 1
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
            if self.beads[self.chosen] == 1:
                self.colours += 1
        elif result == 2:
            self.beads[self.chosen] += 3
            if self.beads[self.chosen] == 3:
                self.colours += 1

    # append
    def write_file(self, filename):
        print("TODO: write box line")
        # f = open(filename)
        # f.write(str(self.beads) + " " + str(self.colours))
        # f.close()

    def read_line(self, line):
        print("TODO: readline")
        # line += " "
        # line.cut(" ")
        # f = open(filename)
        # line = f.readline()
        # f.close()

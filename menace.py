from box import Box
from board import Board


class Menace:
    # Array of boxes
    boxes = {}
    # '000000000': Box(0, board=[0, 0, 0, 0, 0, 0, 0, 0, 0])

    # array of chosen boxes
    chosen = ['000000000', '000000000', '000000000', '000000000']

    # last modified:
    last = -1

    def __init__(self):
        print("I'm the machine learning")

    # returns the position where MENACE wants to move
    # if retun = -1 then no more beads
    def move(self, board):
        if self.last == 3:
            for i in range(0, 9):
                if board.get_board()[i] == 0:
                    position = i
                    return position
        str1 = ''
        for i in range(0, 9):
            str1 += str(board.get_board()[i])
        if str1 not in self.boxes:
            new_board = Board()
            new_board.copy_board(board)
            self.boxes[str1] = Box(1, new_board)
        self.last += 1
        self.chosen[self.last] = str1
        position = self.boxes[str1].move()
        return position

    # return:
    # True - the box already exists
    # False - the box doesn't exist
    def check_box(self, board):
        str1 = ''
        for i in range(0, 9):
            str1 += str(board[i])
        print(str1)
        return str1 in self.boxes

    # result =>
    # loser = 0
    # drawer = 1
    # winner = 2
    def result(self, result):
        for i in range(0, self.last+1):
            self.boxes[self.chosen[i]].result(result)

    def clean(self):
        self.chosen = ['000000000', '000000000', '000000000', '000000000']
        self.last = -1

    # rotations = [(0, 1, 2, 3, 4, 5, 6, 7, 8),
    #              (2, 1, 0, 5, 4, 3, 8, 7, 6),
    #              (6, 7, 8, 3, 4, 5, 0, 1, 2),
    #              (6, 3, 0, 7, 4, 1, 8, 5, 2),
    #              (8, 7, 6, 5, 4, 3, 2, 1, 0),
    #              (2, 5, 8, 1, 4, 7, 0, 3, 6),
    #              (0, 3, 6, 1, 4, 7, 2, 5, 8),
    #              (8, 5, 2, 7, 4, 1, 6, 3, 0)]

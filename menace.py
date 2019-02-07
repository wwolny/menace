from box import Box

# TODO:
# 1. initialize the array of boxes
# 2. fill the move()


class Menace:
    # Array of boxes
    boxes = [Box(1, board=[0, 0, 0, 0, 0, 1, 2, 2, 1])]

    # array of chosen boxes
    chosen = [-1]*4

    def __init__(self):
        print("I'm the machine learning")
        self.initBoxes()

    def init_boxes(self):
        print("I initialize boxes")

    # returns the position where MENACE wants to move
    def move(self, board):
        print("I make a move")
        position = 0
        return position

    # result =>
    # loser = 0
    # drawer = 1
    # winner = 2
    def result(self, result):
        for i in range(0, 5):
            self.boxes[self.chosen[i]].result(result)




from box import Box


class Menace:
    # Array of boxes
    boxes = [Box(1, board=[0, 0, 0, 0, 0, 1, 2, 2, 1])]

    # array of chosen boxes
    chosen = [-1]*4

    def __init__(self):
        print("I'm the machine learning")
        self.initBoxes()

    def initBoxes(self):
        print("I initialize boxes")

    def move(self, board):
        print("I make a move")

    # result =>
    # loser = 0
    # drawer = 1
    # winner = 2
    def result(self, result):
        for i in range(0, 5):
            self.boxes[self.chosen[i]].result(result)




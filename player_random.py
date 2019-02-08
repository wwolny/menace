from random import randint

class Player_Random:
    def __init__(self):
        print("I'm radnomizer")

    def move(self, index, board):
        pos = -1
        tmp = randint(1, index)
        for i in range(0, 9):
            if board[i] == 0:
                if tmp == 1:
                    pos = i
                    break
                else:
                    tmp -= 1
        if pos == -1:
            raise ValueError("Wrong Random")
        return pos

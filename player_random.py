from random import randint
from random import seed

class Player_Random:
    def __init__(self):
        print("I'm radnomizer")
        seed(1000)

    def move(self, index, board):
        pos = self.can_win(board)
        if pos >= 0:
            return pos
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

    def can_win(self, board):
        for i in range(0, 3):
            if board[3*i] + board[3*i+1] + board[3*i+2] == 4:
                if board[3*i] == 0:
                    return 3*i
                elif board[3*i+1] == 0:
                    return 3*i+1
                elif board[3 * i + 2] == 0:
                    return 3 * i + 2
        for i in range(0, 3):
            if board[i] + board[i+3] + board[i+6] == 4:
                if board[i] == 0:
                    return i
                elif board[i+3] == 0:
                    return i+3
                elif board[i + 6] == 0:
                    return i + 6
        if board[0] + board[4] + board[8]:
            if board[0] == 0:
                return 0
            elif board[4] == 0:
                return 4
            elif board[8] == 0:
                return 8
        if board[2] + board[4] + board[5]:
            if board[2] == 0:
                return 2
            elif board[4] == 0:
                return 4
            elif board[5] == 0:
                return 5
        return -1
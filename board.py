#Board:
#012
#345
#678

# x-> 1,2,3
# y
# |
# v
# 1
# 2
# 3


class Board:
    board = [0]*9

    def __init__(self):
        print("Board")

    def get_value(self, x, y):
        x = int(x)
        y = int(y)
        if x > 3 or x < 1 or y < 1 or y > 3:
            raise ValueError("Wrong place in the board")
        return self.board[x+3*(y-1)-1]

    def set_value(self, x, y, value):
        x = int(x)
        y = int(y)
        if x > 3 or x < 1 or y < 1 or y > 3 or value not in [-1, 0, 1]:
            raise ValueError("Wrong place in the board")
        self.board[x+3*(y-1)-1] = value

    # x - last move x
    # y - last move y
    # returns 1 if winner
    # returns 0 if no winner
    def check_winner(self, x, y):
        x = int(x)
        y = int(y)
        if self.board[3*(y-1)] == self.board[3*(y-1)+1] == self.board[3*(y-1)+2]:
            return 0
        elif self.board[x-1] == self.board[x+2] == self.board[x+5]:
            return 0
        elif x == y:
            if self.board[0] == self.board[4] == self.board[8]:
                return 0
            elif x == 2:
                if self.board[2] == self.board[4] == self.board[6]:
                    return 0
        elif (x == 1 and y == 3) or (x == 3 and y == 1):
            if self.board[2] == self.board[4] == self.board[6]:
                return 0
        return 1

    def print_board(self):
        for i in range(0, 3):
            print(self.board[3*i:3*i+3])

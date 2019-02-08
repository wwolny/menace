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

    free = 9

    def __init__(self):
        print("board")

    def copy_board(self, board):
        self.board = board.get_board().copy()

    def get_value_xy(self, x, y):
        x = int(x)
        y = int(y)
        if x > 3 or x < 1 or y < 1 or y > 3:
            raise ValueError("Wrong place in the board")
        return self.board[x+3*(y-1)-1]

    def get_value_pos(self, pos):
        if pos > 8 or pos < 0:
            raise ValueError("Wrong place in the board")
        return self.board[pos]

    def set_value_xy(self, x, y, value):
        x = int(x)
        y = int(y)
        if x > 3 or x < 1 or y < 1 or y > 3 or value not in [0, 1, 2]:
            raise ValueError("Wrong place in the board")
        self.board[x + 3 * (y - 1) - 1] = value
        self.free -= 1

    def set_value_pos(self, position, value):
        position = int(position)
        if position > 8 or position < 0 or value not in [0, 1, 2]:
            raise ValueError("Wrong place in the board")
        self.board[position] = value
        self.free -= 1

    # x - last move x
    # y - last move y
    # returns 1 if winner
    # returns 0 if no winner
    def check_winner_xy(self, x, y):
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

    def check_winner_pos(self, pos):
        pos = int(pos)
        if pos < 3:
            if self.board[0] == self.board[1] == self.board[2]:
                return 0
        elif pos < 6:
            if self.board[4] == self.board[3] == self.board[5]:
                return 0
        else:
            if self.board[6] == self.board[7] == self.board[8]:
                return 0
        if pos in [0, 3, 6]:
            if self.board[0] == self.board[3] == self.board[6]:
                return 0
        elif pos in [1, 4, 7]:
            if self.board[1] == self.board[4] == self.board[7]:
                return 0
        if pos in [2, 5, 8]:
            if self.board[2] == self.board[5] == self.board[8]:
                return 0
        if self.free == 0:
            return -1
        return 1

    def print_board(self):
        for i in range(0, 3):
            print(self.board[3*i:3*i+3])

    def get_board(self):
        return self.board

    def clean(self):
        for i in range(0, 9):
            self.board[i] = 0
        self.free = 9


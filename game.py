from board import Board

# TODO:
# 1)check if value given by the user is valid
# if it's not reask for the value


class Game:
    p1 = 1
    p2 = 2
    board = Board()

    def __init__(self):
        print("game")

    def play(self):
        play = 1
        while play:
            play = self.move()
        if self.p1 > self.p2:
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    # values of P1 are 1's
    # values of P2 are 2's
    def move(self):
        if self.p1 < self.p2:
            print("Player 1 move")
            self.p1 += 2
            lastmovex = input("x = ")
            lastmovey = input("y = ")
            self.board.setvalue(lastmovex, lastmovey, 1)
        else:
            print("Player 2 move")
            self.p2 += 2
            lastmovex = input("x = ")
            lastmovey = input("y = ")
            self.board.setvalue(lastmovex, lastmovey, 2)
        self.board.printboard()
        return self.board.checkwinner(lastmovex, lastmovey)

from game import Game
# from board import Board
# from menace import Menace


def main():
    game = Game()
    results = []
    for j in range(1, 100):
        menace = 0
        random = 0
        draw = 0
        for i in range(1, 100):
            score = game.play()
            if score == 0:
                draw += 1
            elif score == 1:
                menace += 1
            else:
                random += 1
        results.append([menace, random, draw])
    print(results)


    # print("Menace score: ")
    # print(menace)
    # print("Draw score: ")
    # print(draw)
    # print("Random score: ")
    # print(random)


main()

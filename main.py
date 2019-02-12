from game import Game
# from board import Board
# from menace import Menace

FILENAME = "results.csv"

def main():
    results = []
    game = Game()
    results.append(["menace", "random", "draw"])
    for j in range(1, 100):
        menace = 0
        random = 0
        draw = 0
        for i in range(1, 50):
            score = game.play()
            if score == 0:
                draw += 1
            elif score == 1:
                menace += 1
            else:
                random += 1
        results.append([menace, random, draw])
    f = open(FILENAME, "wt")
    for i in range(0, int(len(results))):
        f.write(str(results[i][0]) + ' ' + str(results[i][1]) + ' ' + str(results[i][2]) + '\n')
    f.close()
    print(results)


main()

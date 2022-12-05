with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

games = [[ord(game[0]) - ord("A") + 1, ord(game[2]) - ord("X") + 1] for game in inputs]


def calcGameScore1(game):
    delta = (game[0] - game[1]) % 3
    return game[1] + (3 if delta == 0 else (6 if delta == 2 else 0))


def calcGameScore2(game):
    # switch hands
    if game[1] == 1:
        game[1] = (game[0] - 1) if game[0] - 1 > 0 else 3
    elif game[1] == 2:
        game[1] = game[0]
    else:
        game[1] = (game[0] + 1) if game[0] + 1 < 4 else 1

    return calcGameScore1(game)


score1 = sum(map(calcGameScore1, games))
print("Total score #1: {}".format(score1))

score2 = sum(map(calcGameScore2, games))
print("Total score #2: {}".format(score2))

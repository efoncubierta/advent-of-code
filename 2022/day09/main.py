import math
import numpy as np

with open("input.txt", "r") as f:
    inputs = [(i.split(" ")[0], int(i.split(" ")[1]))
              for i in f.read().splitlines()]

def solve(length):
    moves = []
    for i in range(0, length):
        moves.append([(0, 0)])

    def updateTail():
        for i in range(1, len(moves)):
            offset = (0, 0)
            if math.dist(moves[i-1][-1], moves[i][-1]) >= 2:
                offset = (
                    np.sign(moves[i-1][-1][0] - moves[i][-1][0]),
                    np.sign(moves[i-1][-1][1] - moves[i][-1][1])
                )
            if offset[0] != 0 or offset[1] != 0:
                moves[i].append((
                    moves[i][-1][0] + offset[0],
                    moves[i][-1][1] + offset[1]
                ))

    for input in inputs:
        for i in range(0, input[1]):
            if input[0] == "R":
                moves[0].append((
                    moves[0][-1][0] + 1,
                    moves[0][-1][1]
                ))
            elif input[0] == "L":
                moves[0].append((
                    moves[0][-1][0] - 1,
                    moves[0][-1][1]
                ))
            elif input[0] == "U":
                moves[0].append((
                    moves[0][-1][0],
                    moves[0][-1][1] + 1
                ))
            else:
                moves[0].append((
                    moves[0][-1][0],
                    moves[0][-1][1] - 1
                ))
            updateTail()

    return len(set(["{},{}".format(t[0], t[1]) for t in moves[-1]]))

# Part 1
print("Visited once: {}".format(solve(2)))
# Part 2
print("Visited once: {}".format(solve(10)))

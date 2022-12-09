import numpy as np

with open("input.txt", "r") as f:
    inputs = [(i.split(" ")[0], int(i.split(" ")[1]))
              for i in f.read().splitlines()]

MOVES = {
  "R": np.array([1, 0]),
  "L": np.array([-1, 0]),
  "U": np.array([0, 1]),
  "D": np.array([0, -1])
}

def solve(length):
    moves = []
    for _ in range(0, length):
        moves.append([np.array([0, 0])])

    def updateTail():
        for i, move in enumerate(moves[1:], start=1):
            offset = (0, 0)
            if np.linalg.norm(moves[i-1][-1] - move[-1]) >= 2:
                offset = np.array([
                    np.sign(moves[i-1][-1][0] - move[-1][0]),
                    np.sign(moves[i-1][-1][1] - move[-1][1])
                ])
            if offset[0] != 0 or offset[1] != 0:
                move.append(move[-1] + offset)

    for input in inputs:
        for _ in range(0, input[1]):
            moves[0].append(moves[0][-1] + MOVES[input[0]])
            updateTail()

    return len(set([tuple(t) for t in moves[-1]]))

# Part 1
print("Visited once #1: {}".format(solve(2)))
# Part 2
print("Visited once #2: {}".format(solve(10)))

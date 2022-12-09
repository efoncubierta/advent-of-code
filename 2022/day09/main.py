import math
import numpy as np

with open("input.txt", "r") as f:
    moves = [(i.split(" ")[0], int(i.split(" ")[1]))
             for i in f.read().splitlines()]

# Part 1
#length = 2

# Part 2
length = 10

positions = []
for i in range(0, length):
    positions.append([(0, 0)])

def updateTail():
    for i in range(1, len(positions)):
        offset = (0,0)
        if math.dist(positions[i-1][-1], positions[i][-1]) >= 2:
          offset = (np.sign(positions[i-1][-1][0] - positions[i][-1][0]), np.sign(positions[i-1][-1][1] - positions[i][-1][1]))
        if offset[0] != 0 or offset[1] != 0:
            positions[i].append((positions[i][-1][0] + offset[0], positions[i][-1][1] + offset[1]))

for move in moves:
    for i in range(0, move[1]):
        lastHead = positions[0][-1]
        if move[0] == "R":
            positions[0].append((lastHead[0] + 1, lastHead[1]))
        elif move[0] == "L":
            positions[0].append((lastHead[0] - 1, lastHead[1]))
        elif move[0] == "U":
            positions[0].append((lastHead[0], lastHead[1] + 1))
        else:
            positions[0].append((lastHead[0], lastHead[1] - 1))
        updateTail()

once = len(set(["{},{}".format(t[0], t[1]) for t in positions[-1]]))
print("Visited once: {}".format(once))

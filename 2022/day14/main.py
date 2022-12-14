import numpy as np

with open("input.txt", "r") as f:
    inputs = [
        [
            tuple([
                int(k)
                for k in j.split(",")
            ])
            for j in i.split(" -> ")
        ]
        for i in f.read().split("\n")
    ]

rocks = set()
depth = 0
for path in inputs:
    rocks.add(path[0])
    for i in range(1, len(path)):
        x_offset = path[i][0] - path[i-1][0]
        y_offset = path[i][1] - path[i-1][1]
        depth = depth if path[i][1] <= depth else path[i][1]
        rocks.add(path[i])
        if x_offset != 0:
            for x in range(0, x_offset, np.sign(x_offset)):
                rocks.add((path[i-1][0] + x, path[i-1][1]))
        if y_offset != 0:
            for y in range(0, y_offset, np.sign(y_offset)):
                rocks.add((path[i-1][0], path[i-1][1] + y))

def next(sands, depth, forceDepth=False):
    def isUsed(p):
        return p in sands or p in rocks

    x = 500
    for y in range(0, depth + 1):
        if y == depth:
            return (x, y) if forceDepth else (-1, -1)
        if isUsed((x, y + 1)):
            if not isUsed((x - 1, y + 1)):
                x -= 1
            elif not isUsed((x + 1, y + 1)):
                x += 1
            elif not isUsed((x, y)):
                return (x, y)


# Part 1
sands = set()
while (n := next(sands, depth)) != (-1, -1):
    sands.add(n)
print("Part 1: {}".format(len(sands) + 1))

# Part 2
sands = set()
while (n := next(sands, depth + 1, True)) != (500, 0):
    sands.add(n)
print("Part 2: {}".format(len(sands) + 1))

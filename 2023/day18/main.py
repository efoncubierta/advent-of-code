import numpy as np

with open("input.txt", "r") as file:
    inputs = [
        input.split(" ")
        for input in file.read().split("\n")
    ]

directions = {
    'U': (0, -1),
    '3': (0, -1),
    'L': (-1, 0),
    '2': (-1, 0),
    'D': (0, 1),
    '1': (0, 1),
    'R': (1, 0),
    '0': (1, 0)
}

def volume(part2 = False):
    p = 0
    xs = [0]
    ys = [0]
    for input in inputs:
        d = directions[input[2][-2]] if part2 else directions[input[0]]
        l = int(input[2][2:-2], 16) if part2 else int(input[1])
        p += l
        xs.append(xs[-1] + l*d[0])
        ys.append(ys[-1] + l*d[1])

    a = 0.5*np.abs(np.dot(xs,np.roll(ys,1))-np.dot(ys,np.roll(xs,1)))
    return int((a + 1 - p // 2) + p)


print("Part 1: {}".format(volume()))
print("Part 2: {}".format(volume(True)))
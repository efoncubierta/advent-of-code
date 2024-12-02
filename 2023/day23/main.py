import sys
from functools import cache

sys.setrecursionlimit(1000000)

with open("input.txt", "r") as file:
    MAP = [
        [c for c in input]
        for input in file.read().split("\n")
    ]

h = len(MAP)
w = len(MAP[0])

D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

start = (0, 1)
finish = (w - 2, h - 1)

@cache
def dfs(x, y, s, part2 = False):
    if (x, y) == finish:
        return s
    
    o = MAP[y][x]
    
    MAP[y][x] = 'O'
    longest = 0
    for d in D:
        nx, ny = x + d[0], y + d[1]
        if (
            # in range
            0 <= nx < w and 0 <= ny < h and
            # not forest
            MAP[ny][nx] != '#' and
            # not seen
            MAP[ny][nx] != 'O'
        ):
            if part2 or not (
                # not a slope in the oposite direction
                (nx > x and MAP[ny][nx] == '<') or
                (nx < x and MAP[ny][nx] == '>') or
                (ny > y and MAP[ny][nx] == '^') or
                (ny < y and MAP[ny][nx] == 'v')
            ):
                longest = max(longest, dfs(nx, ny, s + 1, part2))

    MAP[y][x] = o
    return longest

# Part 1
print("Part 1: {}".format(dfs(1, 0, 0)))

# Part 2
print("Part 2: {}".format(dfs(1, 0, 0, True)))
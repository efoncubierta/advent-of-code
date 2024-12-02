import math
from collections import deque

with open("input.txt", "r") as file:
    G = [
        [c for c in input]
        for input in file.read().split("\n")
    ]

# dimensions
h = len(G)
w = len(G[0])

# directions
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]

START = ((int(w/2), int(h/2)))

# given a position, return four new positions in all directions
def map_D(x, y):
    return [
        (x + d[0], y + d[1])
        for d in D
    ]

# Returns number of unique tiles reached on every step
def get_reachability(steps):
    T_C = set([START]) # current tiles
    T_V = set()        # previews tiles visited
    R = [0, 1]         # reached tiles. Pos 1 is start. Pos 0 is to avoid outbound exceptions
    for _ in range(steps):
        # update visited tiles with current tiles
        T_V.update(T_C)
        # navigate to new tiles
        T_C = set([
            (nx, ny)
            for tx, ty in T_C
            for nx, ny in map_D(tx, ty)
            # ignore rocks and seen tiles
            if G[ny % h][nx % w] != '#' and (nx, ny) not in T_V
        ])
        R.append(R[-2] + len(T_C))
    return R[1:]

# Part 1
STEPS = 64
print("Part 1: {}".format(get_reachability(STEPS)[STEPS]))

# # Part 2
STEPS = 26501365
R = get_reachability(w*3)

# every 'garden length' the number of tiles reached multiplies.
#
# STEPS % h = 65, which is half the garden's length. That's in fact
# that max number of steps it'd take to reach a corner from the center
# of the garden (start point). So, starting at 65, get the number of tiles
# reached at 65+n*131, where n=0,1,2
m = STEPS % h
x0 = R[m]            # tiles at step 65
x1 = R[m+w] - R[m]   # tiles between steps 65 and 131+65
x2 = (R[m+2*w] - R[m+w] - x1) # tiles between steps 131+65 and 2*131+65 minus tiles steps < 131

r1 = math.floor(STEPS / h) 
r2 = int(r1*(r1-1)/2)
print("Part 2: {}".format(x0 + x1*r1 + x2*r2))
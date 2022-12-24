with open("input.txt", "r") as f:
    inputs = [
        list(l)
        for l in f.read().splitlines()
    ]

D = ">v<^"
M = [(0, 1), (1, 0), (0, -1), (-1, 0)]
W = len(inputs[0]) - 2
H = len(inputs) - 2

BLIZZARDS = {
    (x-1, y-1, D.index(inputs[x][y]))
    for x, row in enumerate(inputs)
    for y, v in enumerate(row)
    if v != "." and v != "#"
}

B = {}
for i in range(H):
    B[(i, None)] = set()
for i in range(W):
    B[(None, i)] = set()
for b in BLIZZARDS:
    # vertical blizzards
    if b[2] == 0 or b[2] == 2:
        B[(b[0], None)].add(b)
    # horizontal blizzards
    else:
        B[(None, b[1])].add(b)

def available(x, y, n):
    # check all horizontal and vertical blizzards
    # that could potentially move to current position
    for b in B[(x, None)].union(B[(None, y)]):
        if (x, y) == (
            (b[0] + M[b[2]][0] * n) % H,
            (b[1] + M[b[2]][1] * n) % W
        ):
            return False
    return True

def solve(E, F, it):
    tt = 100000000
    Q = [(E[0], E[1], it)]
    S = set()
    while Q:
        x, y, t = Q.pop(0)

        # ignore seen positions or potential time (current + distance) is higher 
        if (x, y, t) in S or (t + abs(E[0] - x) + abs(E[1] - y)) >= tt:
            continue
        S.add((x, y, t))

        # check if in destination
        if (x, y) == F:
            tt = min(tt, t)
            continue

        # add next available positions to the queue
        if x > 0 and available(x - 1, y, t + 1):
            Q.append((x - 1, y, t + 1))
        if x < (H-1) and available(x + 1, y, t + 1):
            Q.append((x + 1, y, t + 1))
        if -1 < x < H and y > 0 and available(x, y - 1, t + 1):
            Q.append((x, y - 1, t + 1))
        if -1 < x < H and y < (W-1) and available(x, y + 1, t + 1):
            Q.append((x, y + 1, t + 1))
        if ((x, y) == E and not Q) or (-1 < x < H and available(x, y, t + 1)):
            Q.append((x, y, t + 1))

    return tt + 1

t1 = solve((-1, 0), (H-1, W-1), 0)
print("Part 1: {}".format(t1))
t2 = solve((H, W-1), (0, 0), t1)
t3 = solve((-1, 0), (H-1, W-1), t2)
print("Part 2: {}".format(t3))

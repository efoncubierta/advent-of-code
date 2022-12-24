with open("input.txt", "r") as f:
    inputs = [
        list(l)
        for l in f.read().splitlines()
    ]

D = ">v<^"
M = [(0, 1), (1, 0), (0, -1), (-1, 0)]

w = len(inputs[0]) - 2
h = len(inputs) - 2

blizzards = {
    (x-1, y-1, D.index(inputs[x][y]))
    for x, row in enumerate(inputs)
    for y, v in enumerate(row)
    if v != "." and v != "#"
}

B = {}
for i in range(h):
    B[(i, None)] = set()
for i in range(w):
    B[(None, i)] = set()
for b in blizzards:
    if b[2] == 0 or b[2] == 2:
        B[(b[0], None)].add(b)
    else:
        B[(None, b[1])].add(b)

def isAvailable(x, y, n):
    if x < 0:
        return True
    for b in B[(x, None)].union(B[(None, y)]):
        if (x, y) == (
            (b[0] + M[b[2]][0] * n) % h,
            (b[1] + M[b[2]][1] * n) % w
        ):
            return False
    return True

def solve(E, F, init):
    ts = 100000000
    Q = [(E[0], E[1], init)]
    S = set()
    while Q:
        x, y, s = Q.pop(0)

        # ignore seen positions or higher time
        if (x, y, s) in S or s >= ts:
            continue
        S.add((x, y, s))

        # check destination
        if (x, y) == F:
            ts = min(ts, s)
            continue

        if x > 0 and isAvailable(x - 1, y, s + 1):
            Q.append((x - 1, y, s + 1))
        if x < (h-1) and isAvailable(x + 1, y, s + 1):
            Q.append((x + 1, y, s + 1))
        if -1 < x < h and y > 0 and isAvailable(x, y - 1, s + 1):
            Q.append((x, y - 1, s + 1))
        if -1 < x < h and y < (w-1) and isAvailable(x, y + 1, s + 1):
            Q.append((x, y + 1, s + 1))
        if ((x, y) == E and not Q) or (-1 < x < h and isAvailable(x, y, s + 1)):  # wait in position
            Q.append((x, y, s + 1))

    return ts + 1

t1 = solve((-1, 0), (h-1, w-1), 0)
print("Part 1: {}".format(t1))
t2 = solve((h, w-1), (0, 0), t1)
t3 = solve((-1, 0), (h-1, w-1), t2)
print("Part 2: {}".format(t3))

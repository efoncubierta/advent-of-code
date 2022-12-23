with open("input.txt", "r") as f:
    positions = set([
        (x, y)
        for y, l in enumerate(f.read().splitlines())
        for x, c in enumerate(list(l))
        if c == "#"
    ])

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
surroundings = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]

# global stats
round = 1
om = 0
posAt10 = set()
while True:
    pp = {}  # proposed positions
    cm = 0  # movements counter
    for i, p in enumerate(positions):
        # check if current position is surrounded by others
        if not any([
            (p[0] + s[0], p[1] + s[1]) in positions
            for s in surroundings
        ]):
            pp[p] = p
            continue

        newP = p
        for i in range(0, len(moves)):
            # next position and its adjacents
            m = moves[(i + om) % len(moves)]
            np = (p[0] + m[0], p[1] + m[1])
            adj = [(
                np[0] - (1 if np[0] == p[0] else 0),
                np[1] - (1 if np[1] == p[1] else 0)
            ), (
                np[0] + (1 if np[0] == p[0] else 0),
                np[1] + (1 if np[1] == p[1] else 0)
            )]
            if np not in positions and adj[0] not in positions and adj[1] not in positions:
                newP = np
                break

        # find collision and restore position for boths
        if newP in pp.keys():
            pp[pp[newP]] = pp[newP]
            del pp[newP]
            pp[p] = p
            cm -= 1
        else:
            pp[newP] = p
            cm += 1

    # goal of part 2
    if cm == 0:
        break

    # stats for part 1
    if round == 11:
        posAt10 = positions

    # update positions, round and move offset
    positions = pp.keys()
    round += 1
    om = (om + 1) % len(moves)

# locate min and max
mi = (0, 0)
ma = (0, 0)
for p in posAt10:
    mi = (min(mi[0], p[0]), min(mi[1], p[1]))
    ma = (max(ma[0], p[0]), max(ma[1], p[1]))

print("Part #1: {}".format((ma[0] - mi[0] + 1) * (ma[1] - mi[1] + 1) - len(posAt10)))
print("Part #2: {}".format(round))

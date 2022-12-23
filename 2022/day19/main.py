import re
from functools import lru_cache

with open("input.txt", "r") as f:
    blueprints = [
        (k[0], k[1], k[2], (k[3], k[4]), (k[5], k[6]))
        for k in [
            [
                int(j)
                for j in re.findall(r"(\d+)", i)
            ]
            for i in f.read().split("\n")
        ]
    ]

@lru_cache(maxsize=None)
def find(blueprint, s, m):
    ro, rc, rb, rg, o, c, b, g, t = s

    if t == 0:
        return g

    # optimisation to discard options
    # from current state, what's the maximum number of geodes I can get?
    #
    # current geodes + (current geode robots * time left) + (number of potential geode robots I can still create)
    #
    # potential robots = (t(t - 1)) / 2 = ... + 10 + 9 + 8 + ... starting at t-1
    if (g + rg*t + (t*(t-1))/2) < m:
        return 0

    next = []
    if o >= blueprint[4][0] and b >= blueprint[4][1]:
        next.append((
            (
                ro, rc, rb, rg + 1,
                o + ro - blueprint[4][0], c + rc, b + rb - blueprint[4][1], g + rg,
                t - 1
            )
        ))
    if o >= blueprint[3][0] and c >= blueprint[3][1] and rb < blueprint[4][1]:
        next.append((
            (
                ro, rc, rb + 1, rg,
                o + ro - blueprint[3][0], c + rc - blueprint[3][1], b + rb, g + rg,
                t - 1
            )
        ))
    if o >= blueprint[2] and rc < blueprint[3][1]:
        next.append((
            (
                ro, rc + 1, rb, rg,
                o + ro - blueprint[2], c + rc, b + rb, g + rg,
                t - 1
            )
        ))
    if o >= blueprint[1] and ro < max(blueprint[2], max(blueprint[3][0], blueprint[4][0])):
        next.append((
            (
                ro + 1, rc, rb, rg,
                o + ro - blueprint[1], c + rc, b + rb, g + rg,
                t - 1
            )
        ))
    next.append((
        (
            ro, rc, rb, rg,
            o + ro, c + rc, b + rb, g + rg,
            t - 1
        )
    ))

    for ns in next:
        m = max(m, find(blueprint, ns, m))

    return m

total = 0
for b in blueprints:
    total += (b[0] * find(b, (1, 0, 0, 0, 0, 0, 0, 0, 24), 0))
print("Part 1: {}".format(total))

total = 1
for b in blueprints[0:3]:
    total *= find(b, (1, 0, 0, 0, 0, 0, 0, 0, 32), 0)
print("Part 2: {}".format(total))
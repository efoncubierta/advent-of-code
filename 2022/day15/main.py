import re
from functools import reduce

with open("input.txt", "r") as f:
    inputs = [
        [(k[0], k[1]), (k[2], k[3])]
        for k in [

            [
                int(j)
                for j in re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", i).groups()
            ]
            for i in f.read().split("\n")
        ]
    ]


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def scan(l, h):
    results = []
    for y in range(l, h+1):
        rangesT = []
        for i in inputs:
            o = abs(i[0][1] - y)
            d = distance(i[0], i[1])
            if o <= d:
                rangesT.append([i[0][0] - (d - o), i[0][0] + (d - o)])

        rangesT.sort()

        ranges = [rangesT[0]]
        for r in rangesT[1:]:
            if ranges[-1][0] <= r[0] and r[1] <= ranges[-1][1]:
                continue
            elif ranges[-1][0] <= r[0] <= ranges[-1][1]:
                ranges[-1][1] = r[1]
            else:
                ranges.append(r)

        results.append((y, ranges))
    return results


# Part 1
# h = 10
h = 2000000
print("Part 1: {}".format(reduce(lambda acc, x: acc + x[1] - x[0], scan(h, h)[0][1], 0)))

# Part 2
l = 0
# h = 20
h = 4000000
p = scan(0, 0)
for s in scan(l, h):
    y = s[0]
    ranges = s[1]

    if len(ranges) == 2 and (ranges[0][1] + 1 != ranges[1][0]):
        p = (ranges[0][1] + 1, y)
        break

print("Part 3: {}".format(p[0] * 4000000 + p[1]))
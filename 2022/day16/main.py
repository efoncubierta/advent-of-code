import time
import re
from functools import reduce

with open("input.txt", "r") as f:
    inputs = [
        [k[0], int(k[1]), k[2].split(", ")]
        for k in
        [
            [
                j
                for j in re.search(r'Valve ([A-Z]{2}) has flow rate\=(\d+) tunnels? leads? to valves? (.*)', i.replace(";", "")).groups()
            ]
            for i in f.read().split("\n")
        ]
    ]

V = [valve for valve, _, _ in inputs]
R = [rate for _, rate, _ in inputs]
VS = [valves for _, _, valves in inputs]

D = [
    [1000] * len(V)
    for _ in range(len(V))
]

# initial distance matrix
for i in range(0, len(V)):
    D[i][i] = 0
    for valve in VS[i]:
        D[i][V.index(valve)] = 1

# total distance matrix (Floyd Warshall)
# https://favtutor.com/blogs/floyd-warshall-algorithm
for i in range(0, len(V)):
    for j in range(0, len(V)):
        for k in range(0, len(V)):
            D[j][k] = min(D[j][k], D[j][i] + D[i][k])

def scan(vi, rs, t, multiple=False):
    maxPressure = 0
    for i, (ri, r) in enumerate(rs):
        # new time left (current time - time to go to closed valve - 1 minute to open the valve)
        tn = (t - D[vi][ri] - 1)
        # ignore if exceeding the time
        if tn < 0:
            continue

        # calculate remaining closed valves
        maxPressure = max(maxPressure, (r * tn + scan(ri, rs[:i] + rs[i+1:], tn, multiple)))

    # if multiple: on every step I stop, and calculate the max pressure the elephant
    # can release given the current state of the valves. I use that as default
    # value to compare with my scan.
    return max(maxPressure, scan(vi, rs, 26, False) if multiple else 0)

now = time.time()
rs = [(ri, r) for ri, r in enumerate(R.copy()) if r > 0]
print("Max pressure #1: {}".format(scan(V.index('AA'), rs, 30)))
print("Time: {}".format(time.time() - now))
rs = [(ri, r) for ri, r in enumerate(R.copy()) if r > 0]
print("Max pressure #2: {}".format(scan(V.index('AA'), rs, 26, True)))
print("Time: {}".format(time.time() - now))
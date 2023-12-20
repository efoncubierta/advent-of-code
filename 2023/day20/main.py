import math
from collections import deque

def parse_module(str):
    ps = str.split(" -> ")
    if ps[0][0] in '%&':
        return (ps[0][1:], ps[0][0], ps[1].split(", "))
    else:
        return (ps[0], None, ps[1].split(", "))

def lcm(ns):
    total = 1
    for n in ns:
        total = (total * n) // math.gcd(n, total)
    return total

with open("input.txt", "r") as file:
    inputs = [
        parse_module(input)
        for input in file.read().split("\n")
    ]

modules = {
    i[0]: [i[1], i[2], False]
    for i in inputs
}

conjunctions = {
    m1: {m2: False for m2 in modules if m1 in modules[m2][1]}
    for m1 in modules
    if modules[m1][0] == '&'
}

PART2_S = {
    c: [0, 0]
    for c in conjunctions['df']
}

def solve(part2 = False):
    C = (0, 0) # signals counter (high, low)
    N = 0      # button pushes
    LCM = []   # in part1, least-common divisor items
    while N == 0 or (not part2 and N < 1000) or (part2 and N < 100000000):
        Q = deque([('broadcaster', modules['broadcaster'][1], False)])
        C = (C[0], C[1]+1)
        N += 1

        while Q:
            source, mods, sig = Q.popleft()

            C = (
                C[0] + (1*len(mods) if sig else 0),
                C[1] + (1*len(mods) if not sig else 0)
            )

            for mod in mods:
                # part 2
                if part2:
                    if mod in PART2_S and not sig:
                        if PART2_S[mod][0] == 2 and PART2_S[mod][1] > 0:
                            LCM.append(N - PART2_S[mod][1])
                        else:
                            PART2_S[mod][0] += 1
                            PART2_S[mod][1] = N
                    if len(LCM) == len(PART2_S.keys()):
                        return lcm(LCM)
                
                # ignore test modules
                if mod not in modules:
                    continue

                type, dest, state = modules[mod]
                if type == '%' and not sig:
                    modules[mod][2] = not state
                    Q.append((mod, dest, not state))
                elif type == '&':
                    conjunctions[mod][source] = sig
                    Q.append((mod, dest, not all(conjunctions[mod].values())))

    return C[0] * C[1]
                    
print("Part 1: {}".format(solve()))
print("Part 2: {}".format(solve(True)))
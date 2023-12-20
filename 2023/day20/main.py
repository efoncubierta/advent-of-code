import math
from collections import deque

def parse_module(str):
    ps = str.split(" -> ")
    if ps[0][0] in '%&':
        return (ps[0][1:], ps[0][0], ps[1].split(", "))
    else:
        return (ps[0], None, ps[1].split(", "))

with open("input.txt", "r") as file:
    inputs = [
        parse_module(input)
        for input in file.read().split("\n")
    ]

# modules
M = {
    i[0]: [i[1], i[2], False]
    for i in inputs
}

# conjunctions
C = {
    m1: {m2: False for m2 in M if m1 in M[m2][1]}
    for m1 in M
    if M[m1][0] == '&'
}

# states for part2 counting
PART2_S = {
    c: [0, 0]
    for c in C['df']
}

def solve(part2 = False):
    S = (0, 0) # signals counter (high, low)
    N = 0      # button pushes
    part2_n = 0
    part2_total = 1 # in part1, least-common divisor items
    while N == 0 or (not part2 and N < 1000) or (part2 and N < 100000000):
        # queue (source, targets, signal)
        Q = deque([('broadcaster', M['broadcaster'][1], False)])
        S = (S[0], S[1]+1)
        N += 1
        while Q:
            source, targets, sig = Q.popleft()

            # increment signal counter
            S = (
                S[0] + (1*len(targets) if sig else 0),
                S[1] + (1*len(targets) if not sig else 0)
            )

            for mod in targets:
                # part 2
                if part2:
                    if mod in PART2_S and not sig:
                        if PART2_S[mod][0] == 2 and PART2_S[mod][1] > 0:
                            n = N - PART2_S[mod][1]
                            part2_n += 1
                            part2_total = (part2_total * n) // math.gcd(n, part2_total)
                            if part2_n == len(PART2_S.keys()):
                                return part2_total
                        else:
                            PART2_S[mod][0] += 1
                            PART2_S[mod][1] = N
                
                # ignore test modules
                if mod not in M:
                    continue

                type, dest, state = M[mod]
                if type == '%' and not sig:
                    M[mod][2] = not state
                    Q.append((mod, dest, not state))
                elif type == '&':
                    C[mod][source] = sig
                    Q.append((mod, dest, not all(C[mod].values())))

    return S[0] * S[1]
                    
print("Part 1: {}".format(solve()))
print("Part 2: {}".format(solve(True)))
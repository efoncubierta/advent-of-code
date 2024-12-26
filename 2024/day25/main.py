with open("input.txt", "r") as f:
    input = [i.split("\n") for i in f.read().split("\n\n")]

h, w = len(input[0]) - 2, len(input[0][0])
LOCKS, KEYS = set(), set()

def convert(s):
    v = [0] * len(s[0])
    for c in range(len(s[0])):
        v[c] = sum([1 for r in range(1, len(s) - 1) if s[r][c] == '#'])
    return tuple(v)

def fit(s1, s2):
    return all(s1[i] + s2[i] <= h for i in range(len(s1)))

for s in input:
    if s[0][0] == '#':
        LOCKS.add(convert(s))
    else:
        KEYS.add(convert(s))

total = sum([1 for k in KEYS for l in LOCKS if fit(k, l)])
print("Part 1:", total)
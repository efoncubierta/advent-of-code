from functools import cmp_to_key

with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

RULES = {tuple([int(p) for p in i.split("|")]) for i in input[0].split("\n")}
UPDATES = [[int(p) for p in i.split(",")] for i in input[1].split("\n")]

def in_order(u):
    for i in range(0, len(u)):
        for p in u[:i]:
            if (u[i], p) in RULES:
                return False
        for p in u[i+1:]:
            if (p, u[i]) in RULES:
                return False
    return True

def pages_cmp(p1, p2):
    if (p1, p2) in RULES:
        return 1
    elif (p2, p1) in RULES:
        return -1
    return 0

total1, total2 = 0, 0
for u in UPDATES:
    if in_order(u):
        total1 += u[len(u) // 2]
    else:
        u.sort(key=cmp_to_key(pages_cmp))
        total2 += u[len(u) // 2]

print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))
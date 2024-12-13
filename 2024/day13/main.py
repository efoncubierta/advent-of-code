import re

with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

p = re.compile(r'(\d+)')

def solve(part2 = False):
    total = 0
    for i in input:
        A, B, C, D, E, F = [int(n) for n in re.findall(p, i)]
        E += 10000000000000 if part2 else 0
        F += 10000000000000 if part2 else 0
        a = (C*F - D*E) / (B*C - A*D)
        b = (B*E - A*F) / (B*C - A*D)
        if a.is_integer() and b.is_integer():
            total += int(a*3 + b)
    return total

print("Part 1: {}".format(solve()))
print("Part 2: {}".format(solve(True)))
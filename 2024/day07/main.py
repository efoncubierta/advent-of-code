with open("input.txt", "r") as f:
    input = f.read().split("\n")

equations = []
for i in input:
    p = i.split(": ")
    equations.append([int(n) for n in ([p[0]] + p[1].split(" "))])

def solve(elems, total, part2 = False):
    if elems[0] > total:
        return None
    
    if len(elems) == 1:
        return elems[0] if elems[0] == total else None
    
    e1 = elems.pop(0)
    e2 = elems.pop(0)
    
    r = solve([e1 + e2] + elems, total, part2)
    if r == total:
        return r
    
    r = solve([e1 * e2] + elems, total, part2)
    if r == total:
        return r
    
    return solve([int("{}{}".format(e1,e2))] + elems, total, part2) if part2 else r
        

total1 = 0
total2 = 0
for eq in equations:
    if solve(eq[1:], eq[0]):
        total1 += eq[0]
    if solve(eq[1:], eq[0], part2=True):
        total2 += eq[0]

print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))
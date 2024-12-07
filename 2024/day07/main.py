with open("input.txt", "r") as f:
    input = f.read().split("\n")

equations = []
for i in input:
    p = i.split(": ")
    equations.append([int(n) for n in ([p[0]] + p[1].split(" "))])

def has_solution(elems, total, part2 = False):
    if elems[0] > total:
        return False
    
    if len(elems) == 1:
        return elems[0] == total
    
    e1 = elems.pop(0)
    e2 = elems.pop(0)
    
    return has_solution([e1 + e2] + elems, total, part2) or \
        has_solution([e1 * e2] + elems, total, part2) or \
        (
            part2 and
            has_solution([int("{}{}".format(e1,e2))] + elems, total, part2)
        )
        
total1, total2 = 0, 0
for eq in equations:
    if has_solution(eq[1:], eq[0]):
        total1 += eq[0]
    if has_solution(eq[1:], eq[0], part2=True):
        total2 += eq[0]

print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))
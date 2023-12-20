import re
from collections import deque

def parse_workflow(str):
    p1 = re.search('([^{]+){([^}]+)}', str)
    return (p1.group(1), parse_rules(p1.group(2)))

def parse_rules(str):
    r_str = str.split(",")

    rules = []
    for r in r_str:
        ps = r.split(":")
        if len(ps) == 1:
            rules.append(('.', None, None, ps[0]))
        else:
            rules.append((ps[0][1], ps[0][0], int(ps[0][2:]), ps[1]))
    
    return rules

def parse_parts(str):
    return {
        ps[0]: int(ps[2:])
        for ps in str[1:-1].split(",")
    }
    
with open("input.txt", "r") as file:
    inputs = file.read().split("\n\n")
    workflows = {
        parse_workflow(i)[0]: parse_workflow(i)[1]
        for i in inputs[0].split("\n")
    }
    parts = [
        parse_parts(i)
        for i in inputs[1].split("\n")
    ]

# Part 1
total = 0
for p in parts:
    c = 'in'
    while c not in ['A', 'R']:
        for (op, part, val, dest) in workflows[c]:
            if op == '.':
                c = dest
                break
            elif op == '<' and p[part] < val:
                c = dest
                break
            elif op == '>' and p[part] > val:
                c = dest
                break
    if c == 'A':
        total += sum(p.values())

print("Part 1: {}".format(total))

# Part 2
Q = deque([('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))])
total = 0
while Q:
    w, xr, mr, ar, sr = Q.pop()
  
    if w == 'A':
        total += (xr[1] - xr[0] + 1) * (mr[1] - mr[0] + 1) * (ar[1] - ar[0] + 1) * (sr[1] - sr[0] + 1)
        continue

    if w == 'R':
        continue

    for (op, part, val, dest) in workflows[w]:
        if op == '.':
            Q.append((dest, xr, mr, ar, sr))
        elif op == '>':
            Q.append((dest,
                        xr if part != 'x' else (max(xr[0], val + 1), xr[1]),
                        mr if part != 'm' else (max(mr[0], val + 1), mr[1]),
                        ar if part != 'a' else (max(ar[0], val + 1), ar[1]),
                        sr if part != 's' else (max(sr[0], val + 1), sr[1])))
            # update ranges for next iteration
            xr = xr if part != 'x' else (xr[0], min(xr[1], val))
            mr = mr if part != 'm' else (mr[0], min(mr[1], val))
            ar = ar if part != 'a' else (ar[0], min(ar[1], val))
            sr = sr if part != 's' else (sr[0], min(sr[1], val))
        elif op == '<':
            Q.append((dest,
                        xr if part != 'x' else (xr[0], min(xr[1], val - 1)),
                        mr if part != 'm' else (mr[0], min(mr[1], val - 1)),
                        ar if part != 'a' else (ar[0], min(ar[1], val - 1)),
                        sr if part != 's' else (sr[0], min(sr[1], val - 1))))
            # update ranges for next iteration
            xr = xr if part != 'x' else (max(xr[0], val), xr[1])
            mr = mr if part != 'm' else (max(mr[0], val), mr[1])
            ar = ar if part != 'a' else (max(ar[0], val), ar[1])
            sr = sr if part != 's' else (max(sr[0], val), sr[1])

print("Part 2: {}".format(total))
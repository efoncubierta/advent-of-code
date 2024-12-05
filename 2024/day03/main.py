import re

with open("input.txt", "r") as f:
    input = f.read()

p = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')

# Part 1
total = 0
for t in re.findall(p, input):
    if t.startswith("mul"):
        n1, n2 = t[4:-1].split(",")
        total += int(n1) * int(n2)

print("Part 1: {}".format(total))

# Part 2
total = 0
do = True
for t in re.findall(p, input):
    if t.startswith("don't"):
        do = False
    elif t.startswith("do"):
        do = True
    elif do and t.startswith("mul"):
        n1, n2 = t[4:-1].split(",")
        total += int(n1) * int(n2)

print("Part 2: {}".format(total))
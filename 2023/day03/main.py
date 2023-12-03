import re
from functools import reduce

with open("input.txt", "r") as f:
    inputs = f.read().split("\n")

h = len(inputs)
w = len(inputs[0])
    
def scan(y, x_start, x_finish, f):
    for x_i in range(x_start, x_finish + 1):
        if f(y, x_i):
            return True
    return False

is_number = lambda y, x: inputs[y][x] >= '0' and inputs[y][x] <= '9'
is_symbol = lambda y, x: inputs[y][x] != '.' and not is_number(y, x)
is_gear   = lambda y, x: inputs[y][x] == '*'

total = 0
numbers = [
    (y, x_start, x_finish, int(input[x_start:x_finish+1]))
    for y, input in enumerate(inputs)
    for (x_start, x_finish) in [
        (m.start(), m.end() - 1)
        for m in re.finditer("\d+", input)
    ]
]

# Part 1
#
for (y, x_start, x_finish, n) in numbers:
    # only numbers with symbols in range are considered
    if (
        (y > 0 and scan(y-1, max(0, x_start - 1), min(w-1, x_finish + 1), is_symbol)) or
        (y < (h-1) and scan(y+1, max(0, x_start - 1), min(w-1, x_finish + 1), is_symbol)) or
        (x_start > 0 and is_symbol(y, x_start - 1)) or
        (x_finish < (w-1) and is_symbol(y, x_finish + 1))
    ):
        total += n

print("Part 1: {}".format(total))

# Part 2
#
total = 0
gears = [
    (y, x)
    for y in range(h)
    for x in range(w)
    if is_gear(y, x)
]
for (y, x) in gears:
    # find all numbers in gear's range
    ns = [
        n[3]
        for n in numbers if (
            (n[1]-1 <= x <= n[2]+1) and
            (n[0]-1 <= y <= n[0]+1)
        )
    ]
    # only gears with two numbers in range are considered
    if len(ns) == 2:
        total += reduce((lambda x, y: x * y), ns)

print("Part 2: {}".format(total))
import re

NUMBERS = {
    'one': '1',
    '1': '1',
    'two': '2',
    '2': '2',
    'three': '3',
    '3': '3',
    'four': '4',
    '4': '4',
    'five': '5',
    '5': '5',
    'six': '6',
    '6': '6',
    'seven': '7',
    '7': '7',
    'eight': '8',
    '8': '8',
    'nine': '9',
    '9': '9'
}

with open("input.txt", "r") as f:
    inputs = f.read().split("\n")

total = 0
for w in inputs:
    p = []
    for n in NUMBERS:
        p.extend([(i, NUMBERS[n]) for i in [m.start() for m in re.finditer(n, w)]])
    p = sorted(p)
    total += int(p[0][1]+p[-1][1])

print(total)

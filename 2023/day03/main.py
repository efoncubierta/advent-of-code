import re
from functools import reduce

with open("input.txt", "r") as file:
    inputs = [line.strip() for line in file.readlines()]

# height and width
h = len(inputs)
w = len(inputs[0])

# check if in a row, the check_f test passes
def in_row(row, col_start, col_end, check_f):
    return any([
        check_f(inputs[row][col])
        for col in range(col_start, col_end + 1)
    ])

# check if check_f passes in range
def in_range(row, col_start, col_end, check_f):
    return (
        row > 0 and 
        in_row(row-1, max(0, col_start - 1), min(w-1, col_end + 1), check_f)
    ) or (
        row < (h-1) and
        in_row(row+1, max(0, col_start - 1), min(w-1, col_end + 1), check_f)
    ) or (
        col_start > 0 and
        check_f(inputs[row][col_start - 1])
    ) or (
        col_end < (w-1) and
        check_f(inputs[row][col_end + 1])
    )

# check whether a position is a number, symbol or gear
is_number = lambda c: c.isdigit()
is_symbol = lambda c: c != '.' and not is_number(c)
is_gear   = lambda c: c == '*'

# total accumulated in calculations
total = 0

# get all numbers by row, column start and column end
numbers = [
    (row, m.start(), m.end() - 1, int(input[m.start():m.end()]))
    for row, input in enumerate(inputs)
    for m in re.finditer("\d+", input)
]

# Part 1
#
total = sum([
    n
    for (row, col_start, col_end, n) in numbers
    # only numbers with symbols in range are considered
    if in_range(row, col_start, col_end, is_symbol)
])

print("Part 1: {}".format(total))

# Part 2
#
total = 0
gears = [
    (row, col)
    for row in range(h)
    for col in range(w)
    if is_gear(inputs[row][col])
]
for (row, col) in gears:
    # find all numbers in gear's range
    ns = [
        n
        for (n_row, n_col_start, n_col_end, n) in numbers
        if (
            (n_col_start-1 <= col <= n_col_end+1) and
            (n_row-1 <= row <= n_row+1)
        )
    ]
    # only gears with two numbers in range are considered
    if len(ns) == 2:
        total += reduce((lambda acc, n: acc * n), ns)

print("Part 2: {}".format(total))
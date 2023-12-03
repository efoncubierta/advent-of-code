import re
from functools import reduce

with open("input.txt", "r") as f:
    inputs = f.read().split("\n")

# height and width
h = len(inputs)
w = len(inputs[0])

# check if in a row, the check_f test passes
def in_row(row, col_start, col_finish, check_f):
    for col in range(col_start, col_finish + 1):
        if check_f(row, col):
            return True
    return False

# check if check_f passes in range
def in_range(row, col_start, col_finish, check_f):
    return (
        row > 0 and 
        in_row(row-1, max(0, col_start - 1), min(w-1, col_finish + 1), check_f)
    ) or (
        row < (h-1) and
        in_row(row+1, max(0, col_start - 1), min(w-1, col_finish + 1), check_f)
    ) or (
        col_start > 0 and
        check_f(row, col_start - 1)
    ) or (
        col_finish < (w-1) and
        check_f(row, col_finish + 1)
    )

# check whether a position is a number, symbol or gear
is_number = lambda row, col: inputs[row][col] >= '0' and inputs[row][col] <= '9'
is_symbol = lambda row, col: inputs[row][col] != '.' and not is_number(row, col)
is_gear   = lambda row, col: inputs[row][col] == '*'

# total accumulated in calculations
total = 0

# get all numbers by row, column start and column finish
numbers = [
    (row, col_start, col_finish, int(input[col_start:col_finish+1]))
    for row, input in enumerate(inputs)
    for (col_start, col_finish) in [
        (m.start(), m.end() - 1)
        for m in re.finditer("\d+", input)
    ]
]

# Part 1
#
for (row, col_start, col_finish, n) in numbers:
    # only numbers with symbols in range are considered
    if in_range(row, col_start, col_finish, is_symbol):
        total += n

print("Part 1: {}".format(total))

# Part 2
#
total = 0
gears = [
    (row, col)
    for row in range(h)
    for col in range(w)
    if is_gear(row, col)
]
for (row, col) in gears:
    # find all numbers in gear's range
    ns = [
        n
        for (n_row, n_col_start, n_col_finish, n) in numbers if (
            (n_col_start-1 <= col <= n_col_finish+1) and
            (n_row-1 <= row <= n_row+1)
        )
    ]
    # only gears with two numbers in range are considered
    if len(ns) == 2:
        total += reduce((lambda n_acc, n: n_acc * n), ns)

print("Part 2: {}".format(total))
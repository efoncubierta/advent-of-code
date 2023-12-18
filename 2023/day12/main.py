import re
from functools import cache

with open("input.txt", "r") as file:
    inputs = [
        (
            [c for c in input.split(" ")[0]],
            [int(n) for n in re.findall("\d+", input.split(" ")[1])]
        )
        for input in file.read().split("\n")
    ]

def solve(springs, numbers):
    @cache
    def find(s_i, n_i, c):
        # if both indexes are at the end, return 1.
        # if no more springs to check, return 0.
        if s_i == len(springs):
            return 1 if n_i == len(numbers) else 0
        
        total = 0
        # current spring is not damaged
        if springs[s_i] != '#':
            # the previous was operational (not counting damages)
            if not c:
                # move to next spring
                total += find(s_i + 1, n_i, 0)
            # the previous was damaged. End counting
            elif n_i < len(numbers) and c == numbers[n_i]:
                total += find(s_i + 1, n_i + 1, 0)
        # current spring is not operational
        if springs[s_i] != '.':
            # consider it damaged (inc counter), and move to next one
            total += find(s_i + 1, n_i, c + 1)
        return total

    return find(0, 0, 0)

# Part 1
total = 0
for (springs, numbers) in inputs:
    t = solve(springs+['.'], numbers)
    total += t

print("Part 1: {}".format(total))

# Part 2
total = 0
for (springs, numbers) in inputs:
    t = solve(((springs+['?'])*5)[:-1]+['.'], numbers*5)
    total += t

print("Part 2: {}".format(total))
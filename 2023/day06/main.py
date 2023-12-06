import re
import math

with open("input.txt", "r") as file:
    inputs = [
        re.findall("\d+", line)
        for line in file.readlines()
      ]

solve = lambda t, d: [
    math.floor(((-t - math.sqrt(pow(t, 2) - 4*d))/-2) - 0.1),
    math.ceil(((-t + math.sqrt(pow(t, 2) - 4*d))/-2) + 0.1)
]

# Part1
total = 1
for i in range(len(inputs[0])):
    s = solve(int(inputs[0][i]), int(inputs[1][i]))
    total *= s[0] - s[1] + 1
print("Part 1: {}".format(total))

# Part 2
s = solve(int(''.join(inputs[0])), int(''.join(inputs[1])))
print("Part 2: {}".format(s[0] - s[1] + 1))
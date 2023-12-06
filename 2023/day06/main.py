import re
import math

with open("input.txt", "r") as file:
    inputs = [
        re.findall("\d+", line)
        for line in file.readlines()
      ]

solutions = lambda t, d: [
    math.floor(((-t - math.sqrt(pow(t, 2) - 4*d))/-2)- 0.001),
    math.ceil(((-t + math.sqrt(pow(t, 2) - 4*d))/-2) + 0.001)
]

# Part1
p1_inputs = [
    [int(d) for d in input]
    for input in inputs
]
total = 1
for i in range(len(p1_inputs[0])):
    s = solutions(p1_inputs[0][i], p1_inputs[1][i])
    total *= s[0] - s[1] + 1

print("Part 1: {}".format(total))

# Part 2
p2_inputs = [
    ''.join(input)
    for input in inputs
]

s = solutions(int(p2_inputs[0]), int(p2_inputs[1]))
print("Part 2: {}".format(s[0] - s[1] + 1))
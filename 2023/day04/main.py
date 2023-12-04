import re

with open("input.txt", "r") as file:
    inputs = [
        line.strip().split(": ")[1].split(" | ")
        for line in file.readlines()
    ]

total = 0
for input in inputs:
    numbers = set(re.findall("\d+", input[0])) & set(re.findall("\d+", input[1]))
    if len(numbers) > 0:
        total += pow(2, len(numbers) - 1)

print("Part 1: {}".format(total))

multipliers = [1] * len(inputs)
for i, input in enumerate(inputs):
    matching = len(set(re.findall("\d+", input[0])) & set(re.findall("\d+", input[1])))
    for j in range(matching):
        multipliers[i+j+1] += multipliers[i]

print("Part 2: {}".format(sum(multipliers)))
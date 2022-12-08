from functools import reduce
import numpy as np

with open("input.txt", "r") as f:
    inputs = [[int(j) for j in list(i)] for i in f.read().splitlines()]

inputsT = np.transpose(inputs)

# Part 1
total = 2*len(inputs) + 2*(len(inputs[0])-2)
for i in range(1, len(inputs) - 1):
    for j in range(1, len(inputs[i]) - 1):
        if inputs[i][j] > max(inputs[i][:j]) or \
                inputs[i][j] > max(inputs[i][j+1:]) or \
                inputs[i][j] > max(inputsT[j][:i]) or \
                inputs[i][j] > max(inputsT[j][i+1:]):
            total += 1

print("Total #1: {}".format(total))

# Part 2
def count(l, v):
    return next(iter([i+1 for i, n in enumerate(l) if n >= v]), len(l))

score = 0
for i in range(1, len(inputs) - 1):
    for j in range(1, len(inputs[i]) - 1):
        values = [
            count([*reversed(inputs[i][:j])], inputs[i][j]),
            count(inputs[i][j+1:], inputs[i][j]),
            count([*reversed(inputsT[j][:i])], inputs[i][j]),
            count(inputsT[j][i+1:], inputs[i][j])
        ]
        total = reduce(lambda acc, n: acc * n, values, 1)
        score = total if total > score else score

print("Total #1: {}".format(score))

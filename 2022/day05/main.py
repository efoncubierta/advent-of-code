from functools import reduce
import numpy as np

with open("input.txt", "r") as f:
    inputs = f.read().split("\n\n")

crates = np.transpose([[y for y in x[1::4]] for x in inputs[0].splitlines()[0:-1]])
crates = [[*reversed([y for y in x if y != " "])] for x in crates]

moves = [[int(y[1]), int(y[3]), int(y[5])] for y in [x.split(" ") for x in inputs[1].splitlines()]]

# Part 1
# for m in moves:
#     crates[m[2]-1].extend(reversed(crates[m[1]-1][-m[0]:]))
#     crates[m[1]-1] = crates[m[1]-1][0:-m[0]]

# Part 2
for m in moves:
    crates[m[2]-1].extend(crates[m[1]-1][-m[0]:])
    crates[m[1]-1] = crates[m[1]-1][0:-m[0]]

result = reduce(lambda acc, c: acc + c[-1], crates, "")

print("Result {}".format(result))

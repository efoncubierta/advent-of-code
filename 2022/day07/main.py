import os

with open("input.txt", "r") as f:
    inputs = [
        [j.split(" ") for j in i.replace("$", "").strip().split("\n")]
        for i in f.read().split("\n$")
    ]

results = {}
paths = []
for i in inputs:
    if i[0][0] == "cd" and i[0][1] == "..":
        paths.pop()
    elif i[0][0] == "cd":
        paths.append(
            os.path.join(paths[-1], i[0][1]) if len(paths) > 0 else i[0][1]
        )
        results[paths[-1]] = 0
    else:
        total = sum([int(y[0]) for y in [x for x in i[1:] if x[0] != "dir"]])
        for p in paths:
            results[p] += total

# Part1
max = 100000
total = sum([v for v in results.values() if v <= max])
print("Total #1: {}".format(total))

# Part2
available = 70000000
required = 30000000
needed = required-(available-results["/"])
total = min([v for v in results.values() if v > needed])
print("Total #2: {}".format(total))

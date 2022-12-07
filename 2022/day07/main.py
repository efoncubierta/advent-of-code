with open("input.txt", "r") as f:
    inputs = [[j.split(" ") for j in i.replace("$", "").strip().split("\n")] for i in f.read().split("\n$")]

results = {}
paths = []
for i in inputs:
    if i[0][0] == "cd" and i[0][1] == "..":
        paths.pop()
    elif i[0][0] == "cd":
        currentPath = "{}{}/".format(paths[-1], i[0][1]) if len(paths) > 0 else i[0][1]
        paths += [currentPath]
        results[currentPath] = 0
    else:
        total = sum([int(y[0]) for y in filter(lambda x: x[0] != "ls" and x[0] != "dir", i)])
        for p in paths:
            results[p] += total

# Part1
total = sum(filter(lambda r: r <= 100000, results.values()))
print("Total <= 100000: {}".format(total))

# Part2
available = 70000000-results["/"]
needed = 30000000-available
toDel = min([*filter(lambda r: r[1] > needed, zip(results.keys(), results.values()))], key=lambda r: r[1])
print("To delete: {} {}".format(toDel[0], toDel[1]))

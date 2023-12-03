from functools import reduce

CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# Part 1
#
data = []
with open("input.txt", "r") as f:
    inputs = f.read().split("\n")
    for i in inputs:
        game = int(i.split(": ")[0].split(" ")[1])
        gdata = [
            (int(sdata.split(" ")[0]), sdata.split(" ")[1])
            for gdata in i.split(": ")[1].split("; ")
            for sdata in gdata.split(", ")
        ]
        inc = True
        for g in gdata:
            if CONSTRAINTS[g[1]] < g[0]:
                inc = False
                break
        if inc is True:
            data.append(game)

print("Part 1: {}".format(sum(data)))

# Part 2
#
total = 0
with open("input.txt", "r") as f:
    inputs = f.read().split("\n")
    for i in inputs:
        gdata = [
            (int(sdata.split(" ")[0]), sdata.split(" ")[1])
            for gdata in i.split(": ")[1].split("; ")
            for sdata in gdata.split(", ")
        ]
        inc = True
        cdata = {}
        for g in gdata:
            if g[1] not in cdata:
                cdata[g[1]] = 0
            if g[0] > cdata[g[1]]:
                cdata[g[1]] = g[0]
        total += reduce((lambda x, y: x * y), cdata.values())

print("Part 2: {}".format(total))

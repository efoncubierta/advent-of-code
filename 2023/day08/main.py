import math

with open("input.txt", "r") as file:
    lines = file.read().split("\n")
    moves = lines[0]
    inputs = {
        line[0:3]: (line[7:10], line[12:15], 0)
        for line in lines[2:]
    }

# # Part 1
c = 0
current = 'AAA'
while current != 'ZZZ':
    for m in moves:
        i = 0 if m == 'L' else 1
        current = inputs[current][i]
        c += 1
        if current == 'ZZZ':
            break

print("Part 1: {}".format(c))

# Part 2
found = False
# find all A's
current = [(a, 0) for a in inputs if a[2] == 'A']
while not found:
    for m in moves:
        i = 0 if m == 'L' else 1
        # find path length to a Z node for every A
        # once found, do not continue with that node
        current = [
            (inputs[cur[0]][i], cur[1] + 1) if cur[0][2] != 'Z' else cur
            for cur in current
        ]
        found = all([cur[0][2] == 'Z' for cur in current])
        if found:
            break

# total steps is the least common divisor of each individual path's length
print("Part 2: {}".format(math.lcm(*[cur[1] for cur in current])))
from matplotlib.path import Path

with open("input.txt", "r") as file:
    inputs = [
        list(input)
        for input in file.read().split("\n")
    ]

h = len(inputs)
w = len(inputs[0])

# moves
NORTH = (0, -1)
SOUTH = (0, 1)
WEST  = (-1, 0)
EAST  = (1, 0)

# allowed moves from each pipe
PIPES = {
    '|': [NORTH, SOUTH],
    '-': [WEST,  EAST],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
    '.': []
}

# find starting point
(start_x, start_y) = [
    (x, y)
    for y in range(h)
    for x in range(w)
    if inputs[y][x] == 'S'
][0]

# guess S
s = []
# if pipe at north can move south, then S can move north
if start_y > 0 and SOUTH in PIPES[inputs[start_y-1][start_x]]:
    s.append(NORTH)
# if pipe at south can move north, then S can move south
if start_y < h - 1 and NORTH in PIPES[inputs[start_y+1][start_x]]:
    s.append(SOUTH)
# if pipe at west can move east, then S can move west
if start_x > 0 and EAST in PIPES[inputs[start_y][start_x-1]]:
    s.append(WEST)
# if pipe at east can move west, then S can move east
if start_x < w - 1 and WEST in PIPES[inputs[start_y][start_x+1]]:
    s.append(EAST)

# find pipe matching allowed movements
for k in PIPES:
    if PIPES[k] == s:
        inputs[start_y][start_x] = k
        break

def left(d):
    return (d[1]*-1, d[0])
def right(d):
    return (d[1], d[0]*-1)
def move(p, d):
    return (p[0] + d[0], p[1] + d[1])

# Part 1
path = [(start_x, start_y)]
c_d = SOUTH # start moving south
while True:
    (c_x, c_y) = path[-1]
    c_p = PIPES[inputs[c_y][c_x]]

    for n_d in [c_d, left(c_d), right(c_d)]:
        (n_x, n_y) = move(path[-1], n_d)

        if (
            0 <= n_x < w and
            0 <= n_y < h and
            n_d in c_p
        ):
            path.append((n_x, n_y))
            c_d = n_d
            break

    if (start_x, start_y) == path[-1]:
        path.pop()
        break

print("Part 1: {}".format(int(len(path) / 2)))

# Part 2
p = Path(path)
total = 0
for y in range(h):
    for x in range(w):
        if (x, y) in path:
            continue
        if p.contains_point((x, y)):
            total += 1

print("Part 2: {}".format(total))
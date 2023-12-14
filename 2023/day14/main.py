import copy

with open("input.txt", "r") as file:
    inputs = [
        [c for c in line]
        for line in file.read().split("\n")
    ]

# dimensions
h = len(inputs)
w = len(inputs[0])

# north, west, south, east
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# rounded rocks
o_rocks = {
    y: [
        x
        for x in range(w)
        if inputs[y][x] == 'O'
    ]
    for y in range(h)
}
# squared rocks
s_rocks = {
    y: set([
        x
        for x in range(w)
        if inputs[y][x] == '#'
    ])
    for y in range(h)
}

# roll a rock given by its coordinates, a direction and a set of existing rounded rocks
def roll(rocks, x, y, d):
    t = 0

    # roll it until reaching the borders or finding a squared rock
    (n_x, n_y) = (x, y)
    while (
        (0 <= n_x + d[0] < w and 0 <= n_y + d[1] < h) and
        (n_x + d[0] not in s_rocks[n_y + d[1]])
    ):
        (n_x, n_y) = (n_x + d[0], n_y + d[1])
        # count the steps
        if n_x in rocks[n_y]:
            t += 1

    # return new position given by last position plus steps
    return (
        n_x - t*d[0] if d[0] else x,
        n_y - t*d[1] if d[1] else y
    )

# tilt the board given a list of rock positions
def tilt(rocks, d):
    # copy to avoid mutation during the iteration
    t_rocks = copy.deepcopy(rocks)
    for y in t_rocks:
        for x in t_rocks[y]:
            (n_x, n_y) = roll(t_rocks, x, y, d)
            rocks[y].remove(x)
            rocks[n_y].append(n_x)

# run a entire cycle of tilts (north, west, south, east)
def cycle(rocks):
    for d in directions:
        tilt(rocks, d)

# Part 1
c_rocks = copy.deepcopy(o_rocks)
tilt(c_rocks, (0, -1))
total = sum([
    len(c_rocks[y])*(h - i)
    for i, y in enumerate(c_rocks)
])
print("Part 1: {}".format(total))

# Part 2
c_rocks = copy.deepcopy(o_rocks)

# iterate until finding a periodic sequence
# first elements might not be periodic
seen = []
first_n = 0
period_n = 0
periodic = False
while True:
    cycle(c_rocks)

    if c_rocks in seen:
        if periodic:
            break
        seen = [copy.deepcopy(c_rocks)]
        periodic = True

    if periodic:
        period_n += 1
    else:
        first_n += 1

    seen.append(copy.deepcopy(c_rocks))

# get the last rocks setup
c_rocks = seen[((1000000000 - first_n) % period_n)]
total = sum([
    len(c_rocks[y])*(h - i)
    for i, y in enumerate(c_rocks)
])
print("Part 2: {}".format(total))
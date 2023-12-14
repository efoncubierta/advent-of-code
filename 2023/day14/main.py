with open("input.txt", "r") as file:
    inputs = [
        [c for c in line]
        for line in file.read().split("\n")
    ]

h = len(inputs)
w = len(inputs[0])

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

o_rocks = {
    y: [
        x
        for x in range(w)
        if inputs[y][x] == 'O'
    ]
    for y in range(h)
}
f_rocks = {
    y: set([
        x
        for x in range(w)
        if inputs[y][x] == '#'
    ])
    for y in range(h)
}

def roll(c_rocks, x, y, d):
    t = 0
    (n_x, n_y) = (x, y)
    while (
        (0 <= n_x + d[0] < w and 0 <= n_y + d[1] < h) and
        (n_x + d[0] not in f_rocks[n_y + d[1]])
    ):
        (n_x, n_y) = (n_x + d[0], n_y + d[1])
        if n_x in c_rocks[n_y]:
            t += 1

    (n_x, n_y) = (
        n_x - t*d[0] if d[0] else x,
        n_y - t*d[1] if d[1] else y
    )
    return (n_x, n_y)

def tilt(c_rocks, d):
    t_rocks = {
        y: c_rocks[y].copy()
        for y in c_rocks
    }
    for y in t_rocks:
        for x in t_rocks[y]:
            (n_x, n_y) = roll(t_rocks, x, y, d)
            c_rocks[y].remove(x)
            c_rocks[n_y].append(n_x)

def cycle(c_rocks):
    for d in directions:
        tilt(c_rocks, d)

# Part 1
c_rocks = {
    y: o_rocks[y].copy()
    for y in o_rocks
}
tilt(c_rocks, (0, -1))

total = sum([
    len(c_rocks[y])*(h - i)
    for i, y in enumerate(c_rocks)
])

print("Part 1: {}".format(total))

# Part 2
c_rocks = {
    y: o_rocks[y].copy()
    for y in o_rocks
}

seen = []
first_n = 0
period_n = 0
periodic = False
while True:
    c_rocks = {
        y: c_rocks[y].copy()
        for y in c_rocks
    }
    cycle(c_rocks)

    if c_rocks in seen:
        if periodic:
            break
        seen = [c_rocks]
        periodic = True

    if periodic:
        period_n += 1
    else:
        first_n += 1

    seen.append(c_rocks)

c_rocks = seen[((1000000000 - first_n) % period_n)]

total = sum([
    len(c_rocks[y])*(h - i)
    for i, y in enumerate(c_rocks)
])

print("Part 2: {}".format(total))
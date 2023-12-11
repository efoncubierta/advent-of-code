with open("input.txt", "r") as file:
    inputs = file.read().split("\n")

# find galaxies
galaxies = [
    (x, y)
    for y, y_r in enumerate(inputs)
    for x, x_c in enumerate(y_r)
    if x_c == '#'
]
# find empty rows
ys = [
    all([x == '.' for x in input])
    for input in inputs
]
# find empty columns
xs = [
    all([
        input[x] == '.'
        for input in inputs
    ])
    for x in range(len(inputs[0]))
]

def distance(g1, g2, factor = 2):
    total_x = sum([
        factor if xs[x] else 1
        for x in range(min(g1[0], g2[0]), max(g1[0], g2[0]))
    ])
        
    total_y = sum([
        factor if ys[y] else 1
        for y in range(min(g1[1], g2[1]), max(g1[1], g2[1]))
    ])

    return total_x + total_y

# Part 1
total = sum([
    distance(g1, g2)
    for i, g1 in enumerate(galaxies)
    for g2 in galaxies[i:]
])
print("Part 1: {}".format(total))

# Part 2
total = sum([
    distance(g1, g2, factor = 1000000)
    for i, g1 in enumerate(galaxies)
    for g2 in galaxies[i:]
])
print("Part 2: {}".format(total))
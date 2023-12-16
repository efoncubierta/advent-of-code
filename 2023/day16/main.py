with open("input.txt", "r") as file:
    grid = [
        [c for c in input]
        for input in file.read().split("\n")
    ]

h = len(grid)
w = len(grid[0])

# Directions: right, down, left, up
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def calc(x, y, d):
    # Keep track of energized tiles
    energized = set()

    tiles = [(x, y, d)]
    while tiles:
        new_tiles = []
        for (x, y, d) in tiles:
            if not (0 <= x < w and 0 <= y < h):
                continue
            
            if (x, y, d) in energized:
                continue

            energized.add((x, y, d))

            # Check the current tile and change direction accordingly
            if grid[y][x] in '/\\':
                # Mirror: changes direction clockwise or counterclockwise
                d = ((3 if grid[y][x] == '/' else 1) - d) % 4
                new_tiles.append((x + dx[d], y + dy[d], d))
            elif grid[y][x] == "-" and (d == 1 or d == 3):
                # Splitter: splits the beam if hitting the flat side
                new_tiles += [(x + dx[0], y + dy[0], 0), (x + dx[2], y + dy[2], 2)]
            elif grid[y][x] == '|' and (d == 0 or d == 2):
                new_tiles += [(x + dx[1], y + dy[1], 1), (x + dx[3], y + dy[3], 3)]
            else:
                new_tiles.append((x + dx[d], y + dy[d], d))
        tiles.clear()
        tiles += new_tiles

    tiles = set([
        (t[0], t[1])
        for t in energized
    ])
    return len(tiles)

# Part 1
print("Part 1: {}".format(calc(0, 0, 0)))

# Part 2
max_tiles = 0
for y in range(h):
    m = calc(0, y, 0)
    if m > max_tiles:
        max_tiles = m
    m = calc(w-1, y, 2)
    if m > max_tiles:
        max_tiles = m
for x in range(w):
    m = calc(x, 0, 1)
    if m > max_tiles:
        max_tiles = m
    m = calc(x, h-1, 3)
    if m > max_tiles:
        max_tiles = m

print("Part 2: {}".format(max_tiles))


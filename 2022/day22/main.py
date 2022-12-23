import re

with open("input.txt", "r") as f:
    inputs = f.read().split("\n\n")

map = [list(i) for i in inputs[0].splitlines()]
path = [(int(i[:-1]), i[-1]) for i in re.findall(r"(\d{1,2}[A-Z])", inputs[1])]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
R, D, L, U = 0, 1, 2, 3

# fix map
w = max([len(row) for row in map])
h = len(map)
map = [row + ([" "] * (w - len(row))) for row in map]

# def wrap(x, y, m):
#     ox, oy = (m[0] * -1, m[1] * -1)

#     nx, ny = (x + ox) % w, (y + oy) % h
#     while map[ny][nx] != " " and 0 < nx < (w - 1) and 0 < ny < (h - 1):
#         nx, ny = (nx + ox) % w, (ny + oy) % h

#     return (nx, ny) if map[ny][nx] != " " else (nx + m[0], ny + m[1])


def wrap(x, y, mi):
    lx, ly = x % 50, y % 50
    xi, yi = x // 50, y // 50

    if (xi, yi) == (1, 0):
        if mi == L:
            return (0, 149 - ly, R)
        if mi == U:
            return (0, 150 + lx, R)

    if (xi, yi) == (2, 0):
        if mi == R:
            return (99, 149 - ly, L)
        if mi == D:
            return (99, 50 + lx, L)
        if mi == U:
            return (lx, 199, U)

    if (xi, yi) == (1, 1):
        if mi == R:
            return (100 + ly, 49, U)
        if mi == L:
            return (ly, 100, D)

    if (xi, yi) == (0, 2):
        if mi == L:
            return (50, 49 - ly, R)
        if mi == U:
            return (50, 50 + lx, R)
        
    if (xi, yi) == (1, 2):
        if mi == R:
            return (149, 49 - ly, L)
        if mi == D:
            return (49, 150 + lx, L)

    if (xi, yi) == (0, 3):
        if mi == R:
          return (50 + ly, 149, U)
        if mi == D:
          return (100 + lx, 0, D)
        if mi == L:
          return (50 + ly, 0, D)


x, y = map[0].index("."), 0
mi = 0
for s, d in path:
    for _ in range(s):
        m = moves[mi]
        nx, ny, nmi = (x + m[0]) % w, (y + m[1]) % h, mi

        if map[ny][nx] == " ":
            (nx, ny, nmi) = wrap(x, y, mi)

        if map[ny][nx] == "#":
            break

        x, y, mi = nx, ny, nmi
    mi = (mi + (1 if d == "R" else -1)) % len(moves)

mi -= 1

l = 0
if mi == L:
    l = 2
elif mi == D:
    l = 1
elif mi == U:
    l = 3

print(1000 * (y + 1) + 4 * (x + 1) + l)

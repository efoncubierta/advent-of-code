with open("input.txt", "r") as f:
    input = [[c for c in i] for i in f.read().split("\n")]

h, w = len(input), len(input[0])
DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

seen = [[False] * w for _ in range(h)]
def bfs(x, y):
    plant = input[y][x]
    area = 0
    fences = set()

    queue = [(x, y)]
    seen[x][y] = True
    while queue:
        c_x, c_y = queue.pop(0)
        area += 1
        for d_i, (d_x, d_y) in enumerate(DIRS):
            n_x, n_y = c_x + d_x, c_y + d_y
            if 0 <= n_x < h and 0 <= n_y < w:
                if input[n_y][n_x] == plant and not seen[n_x][n_y]:
                    seen[n_x][n_y] = True
                    queue.append((n_x, n_y))
                elif input[n_y][n_x] != plant:
                    fences.add((c_x, c_y, d_i))
            else:
                fences.add((c_x, c_y, d_i))
    return area, fences

def sides(fences):
    return sum([
        (x - (d in (1, 3)), y - (d in (0, 2)), d) not in fences
        for (x, y, d) in fences
    ])
                
total1, total2 = 0, 0
for y in range(h):
    for x in range(w):
        if not seen[x][y]:
            area, fences = bfs(x, y)
            total1 += area * len(fences)
            total2 += area * sides(fences)

print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))
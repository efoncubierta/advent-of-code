with open("input.txt", "r") as f:
    input = f.read().split("\n")

w, h = len(input[0]), len(input)

start_x, start_y, end_x, end_y = 0, 0, 0, 0
for y in range(h):
    for x in range(w):
        if input[y][x] == 'S':
            start_x, start_y = x, y
        elif input[y][x] == 'E':
            end_x, end_y = x, y

x, y = start_x, start_y
d_x, d_y = (1, 0)
path = {(x,y): 0}
while True:
    if x == end_x and y == end_y:
        break
    for nd_x, nd_y in [(d_x, d_y), (-d_y, d_x), (d_y, -d_x)]:
        n_x, n_y = x + nd_x, y + nd_y
        if 0 <= n_x < w and 0 <= n_y < h and input[n_y][n_x] != '#':
            x, y = n_x, n_y
            d_x, d_y = nd_x, nd_y
            break
    path[(x, y)] = len(path)

def cheats(max_length=2, min_savings=100):
    total = 0

    for (x1, y1), s1 in path.items():
        # find all points in the path in at max_length distance (a circle)
        # from point (x1, y1) that are ahead of point (x1, y1) in the path, and
        # for each one of them check if a path can be cheated.
        for dx in range(-max_length, max_length + 1):
            for dy in range(-(max_length - abs(dx)), (max_length - abs(dx)) + 1):
                l = abs(dx) + abs(dy)

                x2, y2 = x1 + dx, y1 + dy
                if (x2, y2) != (x1, y1) and (x2, y2) in path and path[(x2, y2)] > s1:
                    s2 = path[(x2, y2)]

                    is_valid = True
                    for step in range(1, l + 1):
                        mx = x1 + (dx * step) // l
                        my = y1 + (dy * step) // l
                        if input[my][mx] == '#':
                            continue
                        elif (mx, my) not in path:
                            is_valid = False
                            break

                    if is_valid and s2 - s1 - l >= min_savings:
                        total += 1

    return total

print("Part 1:", cheats())
print("Part 2:", cheats(max_length=20))
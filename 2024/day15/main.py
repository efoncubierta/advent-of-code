with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

MAP = [[c for c in l] for l in input[0].split("\n")]
MOVS = ''.join(input[1].split("\n"))
DIR = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

def start(map):
    start_x, start_y = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '@':
                start_x, start_y = (x, y)
    return (start_x, start_y)

def gps_sum(map, part2 = False):
    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (not part2 and map[y][x] == 'O') or (part2 and map[y][x] == '['):
                total += (y * 100 + x)
    return total

def extend(map):
    map_e = []
    for y in range(len(map)):
        l = []
        for x in range(len(map[0])):
            l += {"#": "##", "O": "[]", ".": "..", "@": "@."}[map[y][x]]
        map_e.append(l)
    return map_e

def move(map, part2 = False):
    c_x, c_y = start(map)
    for m in MOVS:
        d_x, d_y = DIR[m]
        pos = [(c_x, c_y)]
        wall = False
        for p_x, p_y in pos:
            n_x, n_y = p_x + d_x, p_y + d_y
            if (n_x, n_y) in pos:
                continue
            elif map[n_y][n_x] == '#':
                wall = True
                break
            elif not part2 and map[n_y][n_x] == 'O':
                pos.append((n_x, n_y))
            elif part2 and map[n_y][n_x] in '[]':
                pos += [(n_x, n_y), (n_x + (1 if map[n_y][n_x] == '[' else -1), n_y)]
        if not wall:
            bck = {(x, y): map[y][x] for x, y in pos}
            for x, y in pos:
                map[y][x] = '.'
            for x, y in pos[1:]:
                map[y + d_y][x + d_x] = bck[(x, y)]
            c_x, c_y = c_x + d_x, c_y + d_y
    return map

map1 = move([r.copy() for r in MAP])
print("Part 1: {}".format(gps_sum(map1)))
map2 = move(extend(MAP), True)
print("Part 2: {}".format(gps_sum(map2, True)))
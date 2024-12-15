with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

MAP = [[c for c in l] for l in input[0].split("\n")]
MOVS = ''.join(input[1].split("\n"))
DIR = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

def find_robot(map):
    return [(x, y) for y in range(len(map)) for x in range(len(map[0])) if map[y][x] == '@'][0]

def gps_sum(map):
    return sum([y*100 + x for y in range(len(map)) for x in range(len(map[0])) if map[y][x] in 'O['])

def extend(map):
    map_e = []
    for y in range(len(map)):
        l = []
        for x in range(len(map[0])):
            l += {"#": "##", "O": "[]", ".": "..", "@": "@."}[map[y][x]]
        map_e.append(l)
    return map_e

def move_robot(map):
    c_x, c_y = find_robot(map)
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
            elif map[n_y][n_x] == 'O': # part 1
                pos.append((n_x, n_y))
            elif map[n_y][n_x] in '[]': # part 2
                pos += [(n_x, n_y), (n_x + (1 if map[n_y][n_x] == '[' else -1), n_y)]
        if not wall:
            bck = {(x, y): map[y][x] for x, y in pos}
            for x, y in pos:
                map[y][x] = '.'
            for x, y in pos[1:]:
                map[y + d_y][x + d_x] = bck[(x, y)]
            c_x, c_y = c_x + d_x, c_y + d_y
    return map

print("Part 1: {}".format(gps_sum(move_robot([r.copy() for r in MAP]))))
print("Part 2: {}".format(gps_sum(move_robot(extend(MAP)))))
with open("input.txt", "r") as f:
    input = [[int(n) for n in line] for line in f.read().split("\n")]

h = len(input)
w = len(input[0])

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def crawl(p, pc, nines):
    p_x, p_y = p
    
    if not (0 <= p_x < w and 0 <= p_y < h):
        return
    
    c = input[p_y][p_x]
    if c != (pc + 1):
        return
    
    if c == 9:
        nines.add((p_x, p_y))
        return
    
    for (d_x, d_y) in DIRS:
        crawl((p_x + d_x, p_y + d_y), c, nines)

total = 0
for j in range(h):
    for i in range(w):
        if input[j][i] == 0:
            nines = set()
            crawl((i, j), -1, nines)
            total += len(nines)

print("Part 1: {}".format(total))

def crawl2(p, pc):
    p_x, p_y = p
    
    if not (0 <= p_x < w and 0 <= p_y < h):
        return 0
    
    c = input[p_y][p_x]
    if c != (pc + 1):
        return 0
    
    if c == 9:
        return 1
    
    return sum([crawl2((p_x + d_x, p_y + d_y), c) for (d_x, d_y) in DIRS])

total = 0
for j in range(h):
    for i in range(w):
        if input[j][i] == 0:
            total += crawl2((i, j), -1)

print("Part 2: {}".format(total))
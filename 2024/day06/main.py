from functools import cmp_to_key

with open("input.txt", "r") as f:
    input = [list(s) for s in f.read().split("\n")]

MOVS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

h = len(input)
w = len(input[0])

# initial position and direction
sp_x, sp_y = None, None
sd = None
for y in range(0, h):
    for x in range(0, w):
        i = '^>v<'.find(input[y][x])
        if i >= 0:
            sp_x, sp_y = (x, y)
            sd = i

def next(p_x, p_y, d):
    # move
    np_x, np_y = (p_x + MOVS[d][0], p_y + MOVS[d][1])
    
    # out of bounds
    if not (0 <= np_x < w and 0 <= np_y < h):
        return None
    
    # pivot
    if input[np_y][np_x] == '#':
        d = (d + 1) % len(MOVS)
    else:
        p_x, p_y = (np_x, np_y)
    
    return (p_x, p_y, d)

# Part 1
p_x, p_y, d = sp_x, sp_y, sd
seen = set()
while True:
    seen.add((p_x, p_y))
    
    r = next(p_x, p_y, d)
    if r is None:
        break
    
    p_x, p_y, d = r

print("Part 1: {}".format(len(seen)))

total = 0
for s in seen:
    # ignore start position
    if s[0] == sp_x and s[1] == sp_y:
        continue
    
    # add block
    input[s[1]][s[0]] = '#'
    
    p_x, p_y, d = sp_x, sp_y, sd
    seen_loop = set()
    while True:
        # loop detected
        if (p_x, p_y, d) in seen_loop:
            total += 1
            break
        seen_loop.add((p_x, p_y, d))
    
        r = next(p_x, p_y, d)
        if r is None:
            break
        
        p_x, p_y, d = r
            
    # restore cell
    input[s[1]][s[0]] = '.'
        
print("Part 2: {}".format(total))
    
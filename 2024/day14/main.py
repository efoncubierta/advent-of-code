import re

p = re.compile(r'(-?\d+)')

with open("input.txt", "r") as f:
    input = [[int(n) for n in re.findall(p, i)] for i in f.read().split("\n")]

w, h = 101, 103

q1, q2, q3, q4 = 0, 0, 0, 0
for n_x, n_y, v_x, v_y in input:
    n_x = (n_x + v_x * 100) % w
    n_y = (n_y + v_y * 100) % h

    q1 += n_x < (w - 1) / 2 and n_y < (h - 1) / 2
    q2 += n_x < (w - 1) / 2 and n_y > (h - 1) / 2
    q3 += n_x > (w - 1) / 2 and n_y < (h - 1) / 2
    q4 += n_x > (w - 1) / 2 and n_y > (h - 1) / 2

print("Part 1: {}".format(q1*q2*q3*q4))

i = 1
while True:
    pos = set()
    for n_x, n_y, v_x, v_y in input:
        n_x = (n_x + v_x * i) % w
        n_y = (n_y + v_y * i) % h
        pos.add((n_x, n_y))

    # not great as it is not checking for the entire tree, but it works
    tree = False
    for (p_x, p_y) in pos:
        if (p_x + 1, p_y + 1) in pos and \
            (p_x, p_y + 1) in pos and \
            (p_x - 1, p_y + 1) in pos and \
            (p_x - 2, p_y + 2) in pos and \
            (p_x - 1, p_y + 2) in pos and \
            (p_x , p_y + 2) in pos and \
            (p_x + 1, p_y + 2) in pos and \
            (p_x + 2, p_y + 2) in pos:
            tree = True
            break
         
    if tree:
        break
    i += 1
        
print("Part 2: {}".format(i))
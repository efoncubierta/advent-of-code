with open("input.txt", "r") as f:
    input = [list(i) for i in f.read().split("\n")]

h = len(input)
w = len(input[0])

antennas = list()
for j in range(h):
    for i in range(w):
        if input[j][i] != '.':
            antennas.append((i, j))

def solve(part2 = False):
    antinodes = set()
    for i1 in range(len(antennas)):
        if part2:
            antinodes.add(antennas[i1])
        for i2 in range(i1 + 1, len(antennas)):
            p1_x, p1_y = antennas[i1]
            p2_x, p2_y = antennas[i2]
            
            if input[p1_y][p1_x] != input[p2_y][p2_x]:
                continue

            ox, oy = p1_x - p2_x, p1_y - p2_y
            
            for _ in range(10000000 if part2 else 1):
                nas = True
                p1_x, p1_y = p1_x + ox, p1_y + oy
                if 0 <= p1_x < h and 0 <= p1_y < w:
                    antinodes.add((p1_x, p1_y))
                    nas = False
                p2_x, p2_y = p2_x - ox, p2_y - oy
                if 0 <= p2_x < h and 0 <= p2_y < w:
                    antinodes.add((p2_x, p2_y))
                    nas = False
                if nas:
                    break
    return antinodes

print("Part 1: {}".format(len(solve())))
print("Part 2: {}".format(len(solve(True))))
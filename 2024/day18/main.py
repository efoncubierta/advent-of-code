from collections import deque

with open("input.txt", "r") as f:
    input = [tuple(map(int, l.split(","))) for l in f.read().split("\n")]

SIZE, INITIAL_BYTES = 70, 1024
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

CORRUPTED = set()
for i in input[:INITIAL_BYTES]:
    CORRUPTED.add(i)

def find_shortest_path():
    queue = deque([(0, 0, [])])
    seen = set()
    shortest_path = None
    while queue:
        x, y, p = queue.popleft()
        n_p = p + [(x, y)]

        if x == SIZE and y == SIZE:
            shortest_path = n_p
            break

        for (nd_x, nd_y) in DIRS:
            n_x, n_y = x + nd_x, y + nd_y
            if 0 <= n_x <= SIZE and 0 <= n_y <=SIZE and (n_x, n_y) not in CORRUPTED and (n_x, n_y) not in seen:
                seen.add((n_x, n_y))
                queue.append((n_x, n_y, n_p))
    return shortest_path

shortest_path = find_shortest_path()
print("Part 1:", len(shortest_path) - 1)

for i in input[INITIAL_BYTES:]:
    CORRUPTED.add(i)
    if i in shortest_path: # recalculate only if new fallen byte is blocking current path
        shortest_path = find_shortest_path()
        if shortest_path is None:
            print(f"Part 2: {i[0]},{i[1]}")
            break
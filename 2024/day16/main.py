import heapq

with open("input.txt", "r") as f:
    map = [[c for c in l] for l in f.read().split("\n")]

w, h = len(map[0]), len(map)
start_x, start_y = 1, h - 2
end_x, end_y = w - 2, 1

# state: (cost, x, y, direction, path)
pq = []
heapq.heappush(pq, (0, start_x, start_y, 1, 0, []))
states, best = {}, {}

while pq:
    c, x, y, d_x, d_y, p = heapq.heappop(pq)

    if x == end_x and y == end_y:
        if c not in best:
            best[c] = set()
        best[c].update(p + [(x, y)])
        continue
    
    if (x, y, d_x, d_y) in states and states[(x, y, d_x, d_y)] < c:
        continue

    states[(x, y, d_x, d_y)] = c

    for i, (nd_x, nd_y) in enumerate([(d_x, d_y), (-d_y, d_x), (d_y, -d_x)]):
        n_x, n_y = x + nd_x, y + nd_y
        n_c = c + 1 + (1000 if i > 0 else 0)
        n_p = p + [(x, y)] 
        
        if 0 <= n_x < w and 0 <= n_y < h and map[n_y][n_x] != '#':
            heapq.heappush(pq, (n_c, n_x, n_y, nd_x, nd_y, n_p))

b = min(best.keys())
print("Part 1:", b)
print("Part 2:", len(best[b]))
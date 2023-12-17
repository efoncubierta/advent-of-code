import heapq

with open("input.txt", "r") as file:
    grid = [
        [int(c) for c in input]
        for input in file.read().split("\n")
    ]

h = len(grid)
w = len(grid[0])

# Directions: right, down, left, up
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def calc(part2 = False):
    # Dijkstra

    # priority queue
    pq = []

    # start state: (heat loss, x, y, direction, moves)
    heapq.heappush(pq, (grid[0][0] if part2 else 0, 0, 0, 0, 1))

    # states visited (x, y, direction, moves)
    states = {}

    while pq:
        hl, x, y, d, m = heapq.heappop(pq)

        # return bottom-right corner
        if x == w-1 and y == h-1:
            return hl
        
        # ignore visited states
        if (x, y, d, m) in states:
            continue

        # mark the current state as visited
        states[(x, y, d, m)] = hl

        # move in all directions but backwards
        for i in range(3):
            new_d = (d + i - 1) % 4
            
            # move
            nx, ny = x + dx[new_d], y + dy[new_d]
            new_m = m + 1 if new_d == d else 1

            # check conditions for part1 and part2
            allowed = (
                (not part2 and new_m <= 3) or
                (part2 and new_m <= 10 and (new_d == d or m >= 4))
            )
            
            # add new state if within bounds and allowed
            if 0 <= nx < w and 0 <= ny < h and allowed:
                new_hl = hl + grid[ny][nx]
                new_s = (new_hl, nx, ny, new_d, new_m)
                heapq.heappush(pq, new_s)

print("Part 1: {}".format(calc()))
print("Part 2: {}".format(calc(True)))
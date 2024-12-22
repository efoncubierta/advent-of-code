import heapq

with open("input.txt", "r") as f:
    codes = f.read().strip().split("\n")

NUM_KEYPAD = {
    'A': {'<': '0', '^': '3'},
    '0': {'>': 'A', '^': '2'},
    '1': {'^': '4', '>': '2'},
    '2': {'<': '1', '^': '5', '>': '3', 'v': '0'},
    '3': {'v': 'A', '<': '2', '^': '6'},
    '4': {'^': '7', '>': '5', 'v': '1'},
    '5': {'<': '4', '^': '8', '>': '6', 'v': '2'},
    '6': {'v': '3', '<': '5', '^': '9'},
    '7': {'>': '8', 'v': '4'},
    '8': {'<': '7', '>': '9', 'v': '5'},
    '9': {'v': '6', '<': '8'}
}

DIR_KEYPAD = {
    'A': {'<': '^', 'v': '>'},
    '^': {'>': 'A', 'v': 'v'},
    '<': {'>': 'v'},
    'v': {'<': '<', '^': '^', '>': '>'},
    '>': {'<': 'v', '^': 'A'}
}

PADS = [NUM_KEYPAD] + [DIR_KEYPAD] * 2

cache = {}

def bfs_shortest_paths(pad, start, target):
    pq = [('', start, start)]  # (path, seen, position)

    paths = []
    while pq:
        path, seen, pos = heapq.heappop(pq)

        if pos == target:
            paths.append(path)
            continue

        for move, next_pos in pad[pos].items():
            if next_pos not in seen:
                heapq.heappush(pq, (path + move, seen + next_pos, next_pos))

    return [p for p in paths if len(p) == len(min(paths, key=len))]

def encode(code):
    pq = []
    heapq.heappush(pq, (0, '', 'A', code, 0))  # (cost, path, position, remaining code, pad index)
    visited = {}

    while pq:
        cost, path, pos, r_code, pad_i = heapq.heappop(pq)

        if not r_code:
            if pad_i == len(PADS) - 1:
                return path
            heapq.heappush(pq, (cost, '', 'A', path, pad_i + 1))
            continue

        state = (pad_i, pos, len(r_code), path)
        if state in visited and visited[state] < len(path):
            continue
        visited[state] = len(path)

        if pos == r_code[0]:
            heapq.heappush(pq, (len(path), path + 'A', pos, r_code[1:], pad_i))
        else:
            for p in cache[(pos, r_code[0])]:
                n_path = path + p
                heapq.heappush(pq, (len(n_path) + 2*len(r_code), n_path, r_code[0], r_code, pad_i))

    return None

for pad in [NUM_KEYPAD, DIR_KEYPAD]:
    for start in pad:
        for target in pad:
            if start != target:
                cache[(start, target)] = bfs_shortest_paths(pad, start, target)

total_complexity = 0

for code in codes:
    encoded_path = encode(code)
    if encoded_path:
        length = len(encoded_path)
        numeric_part = int(code[:-1].lstrip('0'))
        complexity = length * numeric_part
        total_complexity += complexity
        # print(code, length)
    else:
        print(f"Failed to encode {code}")

print("Part 1:", total_complexity)

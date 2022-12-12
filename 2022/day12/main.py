with open("input.txt", "r") as f:
    inputs = [list(i) for i in f.read().split("\n")]

start = [
    (i, j) for i in range(0, len(inputs))
    for j in range(0, len(inputs[0])) if inputs[i][j] == 'S'
][0]
inputs[start[0]][start[1]] = 'a'


def minDistance(coord):
    D = []
    for i in range(0, len(inputs)):
        D.append([0] * len(inputs[i]))

    queue = [(coord[0], coord[1], 0)]
    D[coord[0]][coord[1]] = 1
    while len(queue) != 0:
        p = queue.pop(0)

        if inputs[p[0]][p[1]] == 'E':
            return p[2]

        current = inputs[p[0]][p[1]] if (p[0], p[1]) != start else 'a'

        available = []
        if p[1] < (len(inputs[0]) - 1):
            available.append((p[0], p[1]+1))
        if p[1] > 0:
            available.append((p[0], p[1]-1))
        if p[0] < (len(inputs) - 1):
            available.append((p[0]+1, p[1]))
        if p[0] > 0:
            available.append((p[0]-1, p[1]))

        available = [
            x for x in available if
            (
                'a' <= inputs[x[0]][x[1]] <= chr(ord(current) + 1) or
                (current == 'z' and inputs[x[0]][x[1]] == 'E')
            ) and D[x[0]][x[1]] == 0
        ]
        for v in available:
            queue.append((v[0], v[1], p[2] + 1))
            D[v[0]][v[1]] = 1

    return -1


print("Shortest path #1: {}".format(minDistance(start)))

mins = [
    minDistance((r, c)) for r in range(0, len(inputs))
    for c in range(0, len(inputs[0])) if inputs[r][c] == 'a'
]
print("Shortest path #2: {}".format(min([v for v in mins if v > -1])))

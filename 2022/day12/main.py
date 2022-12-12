with open("input.txt", "r") as f:
    inputs = [list(i) for i in f.read().split("\n")]

start = [
    (i, j) for i in range(len(inputs))
    for j in range(len(inputs[0])) if inputs[i][j] == 'S'
][0]
inputs[start[0]][start[1]] = 'a'


def isAvailable(p, n, D):
    return (
        n[0] >= 0 and
        n[0] < len(inputs) and
        n[1] >= 0 and
        n[1] < len(inputs[0])
    ) and (
        'a' <= inputs[n[0]][n[1]] <= chr(ord(inputs[p[0]][p[1]]) + 1) or
        (
            inputs[p[0]][p[1]] == 'z' and inputs[n[0]][n[1]] == 'E'
        )
    ) and D[n[0]][n[1]] == 0


def minDistance(coord):
    D = [[0 for _ in range(len(inputs[0]))] for _ in range(len(inputs))]

    queue = [(coord[0], coord[1], 0)]
    D[coord[0]][coord[1]] = 1
    while len(queue) != 0:
        p = queue.pop(0)

        if inputs[p[0]][p[1]] == 'E':
            return p[2]

        nexts = [
            (n[0], n[1], p[2] + 1)
            for n in [
                (p[0], p[1] + 1),
                (p[0], p[1] - 1),
                (p[0] + 1, p[1]),
                (p[0] + -1, p[1]),
            ] if isAvailable((p[0], p[1]), n, D)
        ]

        for n in nexts:
            queue.append(n)
            D[n[0]][n[1]] = 1

    return -1


print("Shortest path #1: {}".format(minDistance(start)))

print("Shortest path #2: {}".format(min([
    v for v in [
        minDistance((r, c)) for r in range(len(inputs))
        for c in range(len(inputs[0])) if inputs[r][c] == 'a'
    ] if v > -1
])))

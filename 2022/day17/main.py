import math

with open("input.txt", "r") as f:
    moves = list(f.read())

pieces = [
    [4, [
        0b01111000
    ]],
    [3, [
        0b00100000,
        0b01110000,
        0b00100000
    ]],
    [3, [
        0b01110000,
        0b00010000,
        0b00010000
    ]],
    [1, [
        0b01000000,
        0b01000000,
        0b01000000,
        0b01000000
    ]],
    [2, [
        0b01100000,
        0b01100000
    ]]
]


def move(board, x, y, mi, pi):
    (pl, p) = pieces[pi]
    nx = max(0, x - 1) if moves[mi] == "<" else min(7 - pl, x + 1)
    ny = max(0, y - 1)

    # can move sideways?
    for yi, pr in enumerate(p):
        if (y + yi) >= len(board):
            continue
        if board[y + yi] & (pr >> nx):
            nx = x
            break

    # can move downwards?
    for yi, pr in enumerate(p):
        if (y + yi) > len(board) or len(board) == 0:
            continue

        if board[y + yi - 1] & (pr >> nx):
            ny = y
            break

    return (nx, ny)


def run(n):
    board = []
    m = 0
    prev = (0, 0, 0)
    for i in range(0, n):
        pi = i % 5
        (x, y, (_, p)) = (2, len(board) + 3, pieces[pi])
        falling = True
        while falling:
            for mi in range(m % len(moves), len(moves)):
                m += 1
                (x, ny) = move(board, x, y, mi, pi)

                if ny == y:
                    falling = False
                    break

                falling = True
                y = ny

        for yi, pr in enumerate(p):
            pr = pr >> x
            if (y + yi) >= len(board):
                board.append(pr)
            else:
                board[y + yi] |= pr

        if len(board) > 1 and board[-1] == board[0] and pi == 0:
            if prev == (0, 0, 0):
                prev = (m % len(moves), i, len(board))
            elif prev[0] == (m % len(moves)):
                return (i - prev[1], len(board) - prev[2])

    return (n, len(board))


# Part 1
n = 2022
(cycle, count) = run(n)
(_, count2) = run(n % cycle)
print("Part #1: {}".format(count * math.floor(n / cycle) + count2))

# Part 2
n = 1000000000000
(cycle, count) = run(n)
(_, count2) = run(n % cycle)
print("Part #2: {}".format(count * math.floor(n / cycle) + count2))

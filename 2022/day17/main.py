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
        if (y + yi) < len(board) and board[y + yi] & (pr >> nx):
            nx = x
            break

    # can move downwards?
    for yi, pr in enumerate(p):
        if len(board) and (y + yi) <= len(board) and board[y + yi - 1] & (pr >> nx):
            ny = y

    return (nx, ny)


def run(n):
    board = []
    m = 0
    cycle = (0, 0, 0)
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

        # find cycles in the board for first line and piece
        if len(board) > 1 and board[-1] == board[0] and pi == 0:
            # capture first coincidence
            if cycle == (0, 0, 0):
                cycle = (m % len(moves), i, len(board))
            # capture second coincidence
            elif cycle[0] == (m % len(moves)):
                iterations = i - cycle[1]
                length = len(board) - cycle[2]
                # estimate length and calculate remaining moves
                return length * math.floor(n / iterations) + run(n % iterations)

    return len(board)


# Part 1
print("Part #1: {}".format(run(2022)))

# Part 2
print("Part #2: {}".format(run(1000000000000)))

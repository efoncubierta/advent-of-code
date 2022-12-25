import math

with open("input.txt", "r") as f:
    inputs = [
        list(l)
        for l in f.read().splitlines()
    ]

C = "012=-"
V = [0, 1, 2, -2, -1]

def snafu2dec(snafu):
    dec = 0
    for i, c in enumerate(reversed(snafu)):
        n = 0
        if c == "-":
            n = -1
        elif c == "=":
            n = -2
        else:
            n = int(c)
        dec += pow(5, i)*n
    return dec

def dec2snafu(dec):
    snafu = ""
    while dec > 0:
        v = V[dec % 5]
        snafu = C[dec % 5] + snafu
        dec -= v
        dec = math.floor(dec / 5)
    return snafu

total = 0
for snafu in inputs:
    total += snafu2dec(snafu)

print("Part 1: {}".format(total))
print("Part 2: {}".format(dec2snafu(total)))

from collections import Counter

with open("input.txt", "r") as f:
    inputs = f.read().split("\n")

x, y = [], []

for r in inputs:
    rp = r.split()
    x.append(int(rp[0]))
    y.append(int(rp[1]))

x = sorted(x)
y = sorted(y)

total = 0
for i in range(0, len(x)):
    total += abs(x[i] - y[i])

print("Part 1: {}".format(total))

xcount = Counter(x)
ycount = Counter(y)

total = 0
for xn, xc in xcount.items():
    if xn in ycount:
        total += xn * xc * ycount[xn]

print("Part 2: {}".format(total))
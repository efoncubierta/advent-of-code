
def parse_brick(str):
    ps = str.split("~")
    ps0 = [int(c) for c in ps[0].split(",")]
    ps1 = [int(c) for c in ps[1].split(",")]

    return ((ps0[0], ps0[1], ps0[2]), (ps1[0], ps1[1], ps1[2]))

with open("input.txt", "r") as file:
    B = [
        parse_brick(input)
        for input in file.read().split("\n")
    ]

# sort by 'z' before stacking
B = sorted(B, key=lambda x: min(x[0][2], x[1][2]))

# once in order, set z as (0, height)
B = [
    (
        [p1[0], p1[1], 0],
        [p2[0], p2[1], p2[2] - p1[2] + 1]
    )
    for p1, p2 in B
]

# stack bricks in final positions
BS = set()
SS = [None] * len(B)
for i, (p1, p2) in enumerate(B):
    b = set([
        (x, y)
        for x in range(p1[0], p2[0] + 1)
        for y in range(p1[1], p2[1] + 1)
    ])

    o = 0
    bs = set()
    for j in reversed(range(i)):
        pp1, pp2 = B[j]
        if any([
            (x, y) in b
            for x in range(pp1[0], pp2[0] + 1)
            for y in range(pp1[1], pp2[1] + 1)
        ]):
            bs.add(j)
            o = max(o, max(pp1[2], pp2[2]))
    
    B[i][0][2] = o + B[i][0][2]
    B[i][1][2] = o + B[i][1][2]
    SS[i] = set([bbs for bbs in bs if B[bbs][1][2] == o])

    for (x, y) in b:
        for z in range(p1[2], p2[2] + 1):
            BS.add((x, y, o + z))

# Part 1
total = len(B) - len(set.union(*(i for i in SS if len(i) < 2)))
print("Part 1: {}".format(total))

cascade = [None] * len(B)
for i in range(len(B)):
	fallen = {i}
	for j in range(i + 1, len(B)):
		if not SS[j] - fallen:
			fallen.add(j)
	cascade[i] = len(fallen) - 1
print(sum(cascade))
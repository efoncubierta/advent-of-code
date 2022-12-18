with open("input.txt", "r") as f:
    droplets = set([
        tuple([
            int(j)
            for j in i.split(",")
        ])
        for i in f.read().splitlines()
    ])

def addT(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1], t1[2]+t2[2])

# calculate total surface
total = 6 * len(droplets)
# and substract -2 per adjacent droplets
for droplet in droplets:
    for adj in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        if addT(droplet, adj) in droplets:
            total -= 2

# define a volume containing al droplets
minmax = (
    (100000, 100000, 100000),
    (0, 0, 0)
)
for droplet in droplets:
    minmax = ((
        min(minmax[0][0], droplet[0] - 2),
        min(minmax[0][1], droplet[1] - 2),
        min(minmax[0][2], droplet[2] - 2)
    ), (
        max(minmax[1][0], droplet[0] + 2),
        max(minmax[1][1], droplet[1] + 2),
        max(minmax[1][2], droplet[2] + 2)
    ))

# crawl the volumen and find all cubes outside
outside = set()
adjs = [minmax[0]]
while adjs:
    o = adjs.pop()
    # ignore if already counted outside or it's a droplet
    if o in outside or o in droplets:
        continue
    outside.add(o)

    # crawl in all directions
    for adj in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        a = addT(o, adj)
        if minmax[0][0] <= a[0] < minmax[1][0] and \
                minmax[0][1] <= a[1] < minmax[1][1] and \
                minmax[0][2] <= a[2] < minmax[1][2]:
            adjs.append(a)

# calculate total surface in contact with the ouside
totalOutside = 0
for droplet in droplets:
    # only need to count in three direction if adjacent is outside
    for adj in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        if addT(droplet, adj) in outside:
            totalOutside += 2

print("Part #1: {}".format(total))
print("Part #2: {}".format(totalOutside))

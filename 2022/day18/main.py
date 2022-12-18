with open("input.txt", "r") as f:
    droplets = set([
        tuple([
            int(j)
            for j in i.split(",")
        ])
        for i in f.read().splitlines()
    ])

total = 6 * len(droplets)

for droplet in droplets:
    # only need to count in three directions
    for adj in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        if (droplet[0]+adj[0], droplet[1]+adj[1], droplet[2]+adj[2]) in droplets:
            total -= 2

print("Part #1: {}".format(total))

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
        if minmax[0][0] <= o[0] + adj[0] < minmax[1][0] and \
                minmax[0][1] <= o[1] + adj[1] < minmax[1][1] and \
                minmax[0][2] <= o[2] + adj[2] < minmax[1][2]:
            adjs.append((o[0] + adj[0], o[1] + adj[1], o[2] + adj[2]))

totalOutside = 0
for droplet in droplets:
    # only need to count in three direction if adjacent is outside
    for adj in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        if (droplet[0]+adj[0], droplet[1]+adj[1], droplet[2]+adj[2]) in outside:
            totalOutside += 2

print("Part #2: {}".format(totalOutside))

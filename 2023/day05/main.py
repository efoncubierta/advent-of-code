import re

with open("input.txt", "r") as file:
    inputs = file.read().split("\n\n")

maps = []
for input in inputs:
    m = re.search("([^:]+):\n? ?(.*)", input, re.DOTALL)
    mn = [
        [int(n) for n in x.split(" ")]
        for x in m.group(2).split("\n")
    ]
    mn.sort(key=lambda x: x[1])
    maps.append(mn)

# Part 1
def mapNext(v, map):
    for m in map:
        if m[1] <= v < (m[1] + m[2]):
            return m[0] + (v - m[1])
    return v

result = []
for s in maps[0][0]: # seeds
    for m in maps[1:]: # maps
        s = mapNext(s, m)
    result.append(s)

print("Part 1: {}".format(min(result)))

def mapRange(r_start, r_length, map):
    rs = []

    r_end = r_start + r_length

    # is below first range
    if r_start < map[0][1]:
        if r_end < map[0][1]:
            rs.append((r_start, r_length))
            return rs
        else:
            rs.append((r_start, m[0][1] - r_start))
            r_start = m[0][1]

    # iterate over maps
    for m in map:
        # source start and end values
        s_start = m[1]
        s_length = m[2]
        s_end = s_start + s_length
        if s_start <= r_start < s_end:
            delta = (r_start - s_start)
            # new destination start
            n_d_start = m[0] + delta
            if r_end < s_end:
                rs.append((n_d_start, r_length))
                r_length = 0
                break
            else:
                rs.append((n_d_start, s_length - delta))
                r_start = s_end
                r_length = r_length - s_length - delta

    # is above last range
    if r_length > 0:
        rs.append((r_start, r_length))

    return rs

rs = [
    (maps[0][0][i], maps[0][0][i + 1])
    for i in range(0, len(maps[0][0]), 2)
]

for m in maps[1:]:
    rs = [
        nr
        for r in rs
        for nr in mapRange(r[0], r[1], m)
    ]

print("Part 2: {}".format(sorted(rs)[0][0]))
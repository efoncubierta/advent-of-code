import re

def parse_block(block):
    m = re.search("([^:]+):\n? ?(.*)", block, re.DOTALL)
    return sorted([
        [int(n) for n in line.split(" ")]
        for line in m.group(2).split("\n")
    ], key=lambda x: x[1])


with open("input.txt", "r") as file:
    maps = [
        parse_block(block)
        for block in file.read().strip().split("\n\n")
    ]

# Part 1
rs = maps[0][0] # initial values

# iterate over all maps mapping current values
for m in maps[1:]:
    rs = [
        d_start + (r - s_start)
        for r in rs
        for d_start, s_start, length in m
        if s_start <= r < (s_start + length)
    ]
print("Part 1: {}".format(min(rs)))

# Part 2
def mapRange(r_start, r_length, map):
    rs = []

    # r_start and r_length are the initial range start and length values.
    # This algorithms generates a list of ranges in the given map,
    # considering overlapping ranges and ranges outside of the map.
    # 
    # For example,
    #
    # r_start = 5
    # r_length = 10
    # map = [[12, 10, 10]]
    #
    # returns [[5, 5], [12, 5]]
    #
    # total lengths in resulting ranges is = r_length


    # end of the initial range
    r_end = r_start + r_length

    # is below first range in the map
    if r_start < map[0][1]:
        if r_end < map[0][1]:
            # both values are below first range
            # no need to check further
            return [(r_start, r_length)]
        else:
            rs.append((r_start, m[0][1] - r_start))
            r_start = m[0][1]
            r_length -= m[0][1] - r_start

    # iterate over maps
    for (d_start, s_start, length) in map:
        # source start and end values
        s_end = s_start + length
        if s_start <= r_start < s_end:
            delta = (r_start - s_start)
            # new destination start
            n_d_start = d_start + delta

            # all values contains in current range, no overlapping
            if r_end < s_end:
                rs.append((n_d_start, r_length))
                r_length = 0
                break
            # overlapping, add sub-range and move to next range in map
            else:
                rs.append((n_d_start, length - delta))
                r_start = s_end
                r_length -= length - delta

    # is above last range in the map
    if r_length > 0:
        # add remaining range
        rs.append((r_start, r_length))

    return rs

# initial list of ranges
rs = [
    (maps[0][0][i], maps[0][0][i + 1])
    for i in range(0, len(maps[0][0]), 2)
]

# map list of ranges to new ranges
for m in maps[1:]:
    rs = [
        nr
        for r in rs
        for nr in mapRange(r[0], r[1], m)
    ]

print("Part 2: {}".format(sorted(rs)[0][0]))
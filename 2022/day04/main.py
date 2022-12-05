with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

values = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in inputs]

def inRange1(v1, v2):
    return (v1[0] <= v2[0] and v1[1] >= v2[1]) or (v2[0] <= v1[0] and v2[1] >= v1[1])

def inRange2(v1, v2):
    return (v2[0] <= v1[0] <= v2[1]) or (v2[0] <= v1[1] <= v2[1]) or (v1[0] <= v2[0] <= v1[1]) or (v1[0] <= v2[1] <= v1[1])

total1 = len([*filter(lambda v: inRange1(v[0], v[1]), values)])
print("Total overlaps #1: {}".format(total1))

total2 = len([*filter(lambda v: inRange2(v[0], v[1]), values)])
print("Total overlaps #2: {}".format(total2))

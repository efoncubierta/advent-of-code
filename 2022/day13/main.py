import math
import numpy as np
import json


def cmp_to_key(cmp):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return cmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return cmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return cmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return cmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return cmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return cmp(self.obj, other.obj) != 0
    return K


with open("input.txt", "r") as f:
    inputs = [
        [json.loads(j) for j in i.split("\n")]
        for i in f.read().split("\n\n")
    ]


def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return np.sign(p1 - p2)

    p1 = [p1] if isinstance(p1, int) else p1
    p2 = [p2] if isinstance(p2, int) else p2

    for i in range(len(p1)):
        if i == len(p2):
            break
        b = compare(p1[i], p2[i])
        if b < 0 or b > 0:
            return b

    if len(p1) < len(p2):
        return -1

    if len(p2) < len(p1):
        return 1

    return 0


print("Part #1: {}".format(sum([
    i + 1
    for i, packets in enumerate(inputs)
    if compare(packets[0], packets[1]) <= 0
])))

packets = sorted(
    [
        packet
        for packets in inputs
        for packet in packets
    ] + [[2], [6]],
    key=cmp_to_key(compare)
)
print("Part #2: {}".format(math.prod([
    i+1
    for i in range(len(packets))
    if packets[i] == [2] or packets[i] == [6]
])))

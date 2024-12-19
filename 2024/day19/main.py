from functools import lru_cache

with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

patterns = input[0].split(", ")
designs = input[1].split("\n")

def count(design):
    if design == "":
        return 1
    return sum([count(design[:-len(p)]) for p in patterns if design.endswith(p)])

count = lru_cache(maxsize=None)(count)

posibilities = [count(d) for d in designs]
print("Part 1:", len(list(filter(lambda x: x > 0, posibilities))))
print("Part 2:", sum(posibilities))
from functools import lru_cache

with open("input.txt", "r") as f:
    stones = f.read().split(" ")

def count(n, i):
    if i == 0:
        return 1
    elif n == '0':
        return count('1', i - 1)
    elif len(n) % 2 == 0:
        return count(n[:(len(n)//2)], i - 1) + count(str(int(n[len(n)//2:])), i - 1)  
    return count(str(int(n) * 2024), i - 1)

count = lru_cache(maxsize=None)(count)

print("Part 1: {}".format(sum([count(n, 25) for n in stones])))
print("Part 2: {}".format(sum([count(n, 75) for n in stones])))
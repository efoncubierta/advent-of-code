with open("input.txt", "r") as f:
    stones = f.read().split(" ")

seen = {}
def count(n, i):
    if i == 0:
        return 1
    
    if not (n, i) in seen:
        if n == '0':
            seen[(n, i)] = count('1', i - 1)
        elif len(n) % 2 == 0:
            seen[(n, i)] = count(n[:(len(n)//2)], i - 1) + count(str(int(n[len(n)//2:])), i - 1)
        else:
            seen[(n, i)] = count(str(int(n) * 2024), i - 1)
        
    return seen[(n, i)]

total1, total2 = 0, 0
for n in stones:
    total1 += count(n, 25)
    total2 += count(n, 75)

print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))
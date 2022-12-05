from functools import reduce

with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

def accScore(acc, inputs):
    return acc + [
        ord(a) - ord('A') + 27 if ord(a) < ord('a') else ord(a) - ord('a') + 1
        for a in inputs[0] if all(a in line for line in inputs[1:])
    ][0]

score1 = reduce(accScore, [[line[:len(line) // 2], line[len(line) // 2:]] for line in inputs], 0)
print("Total score #1: {}".format(score1))

score2 = reduce(accScore, [inputs[i:i + 3] for i in range(0, len(inputs), 3)], 0)
print("Total score #2: {}".format(score2))

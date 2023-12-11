with open("input.txt", "r") as file:
    inputs = [
        [int(c) for c in line.split(" ")]
        for line in file.read().split("\n")
    ]

def solve(seq):
    if not any(seq):
        return seq + [0]
    
    nseq = [
        seq[i] - seq[i-1]
        for i in range(1, len(seq))
    ]

    return seq + [seq[-1] + solve(nseq)[-1]]

# Part 1
total = sum([solve(input)[-1] for input in inputs])
print("Part 1: {}".format(total))

# Part 2
total = sum([solve(list(reversed(input)))[-1] for input in inputs])
print("Part 2: {}".format(total))
with open("input.txt", "r") as file:
    inputs = [
        [int(c) for c in line.split(" ")]
        for line in file.read().split("\n")
    ]

def solve(seq, backwards=False):
    if not any(seq):
        return seq + [0]
    
    nseq = [
        seq[i] - seq[i-1]
        for i in range(1, len(seq))
    ]

    if backwards:
        return [seq[0] - solve(nseq, backwards)[0]] + seq
    else:
        return seq + [seq[-1] + solve(nseq)[-1]]    

# Part 1
total = 0
for input in inputs:
    total += solve(input)[-1]
print("Part 1: {}".format(total))

# Part 2
total = 0
for input in inputs:
    total += solve(input, backwards=True)[0]
print("Part 2: {}".format(total))
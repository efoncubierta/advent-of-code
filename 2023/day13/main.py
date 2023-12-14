import numpy as np

with open("input.txt", "r") as file:
    inputs = [
        np.array([[c for c in line] for line in block.split("\n")])
        for block in file.read().split("\n\n")
    ]

def solve(input_block, part2=False):
    threshold = 1 if part2 else 0

    def find(block, i_left, i_right, c = 0):
        if c > 1:
            return -1
        
        t = len(block) - sum(block[:, i_left] == block[:, i_right])
        i_found = -1
        if t <= threshold:
            nc = c + t
            
            if i_left == 0 or i_right == len(block[0]) - 1:
                i_found = i_left if nc == threshold else -1
            elif find(block, i_left - 1, i_right + 1, nc) > -1:
                i_found = i_left
        
        if i_found > -1:
            return i_found
        
        if i_right - i_left == 1 and i_right < len(block[0]) -1:
            return find(block, i_left + 1, i_right + 1, 0)
        
        return -1

    c = find(input_block, 0, 1)
    r = find(input_block.transpose(), 0, 1)
    if r != -1:
        return (r+1)*100
    return c + 1

# Part 1
total = sum([
    solve(block)
    for block in inputs
])

print("Part 1: {}".format(total))

# Part 2
total = sum([
    solve(block, True)
    for block in inputs
])

print("Part 2: {}".format(total))
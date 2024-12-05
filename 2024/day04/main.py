import itertools

with open("input.txt", "r") as f:
    input = f.read().split("\n")

WORD = 'XMAS'
WORDS = [WORD[1:], WORD[::-1][:-1]]
DIRECTIONS = [(x, y) for x in [-1, 0, 1] for y in [-1 , 0, 1]]

h = len(input)
w = len(input[0])

def get_word(x, y, d, l):
    if l == 0 or not 0 <= x < w or not 0 <= y < h:
        return ''
    return input[y][x] + get_word(x + d[0], y + d[1], d, l - 1)

total1 = 0
total2 = 0
for y in range(0, h):
    for x in range(0, w):
        # Part 1
        if input[y][x] == WORD[0]:
            for d in DIRECTIONS:
                total1 += 1 if get_word(x, y, d, len(WORD)) == WORD else 0
        # Part 2
        elif input[y][x] == 'A' and 0 < x < (w - 1) and 0 < y < (h - 1):

            w1 = input[y-1][x-1] + input[y][x] + input[y+1][x+1]
            w2 = input[y+1][x-1] + input[y][x] + input[y-1][x+1]

            total2 += 1 if w1 in WORDS and w2 in WORDS else 0

print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))
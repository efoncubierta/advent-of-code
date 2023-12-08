from functools import cmp_to_key

C_VALUES = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

with open("input.txt", "r") as file:
    inputs = [
        line.split(" ")
        for line in file.read().split("\n")
      ]

def hand_score(hand, partTwo=False):
    # count card appearances
    hc = {}
    for h in hand:
        if partTwo and h == 'J':
            continue
        if h not in hc:
            hc[h] = 0
        hc[h] += 1
    cs = sorted(list(hc.values()), reverse=True)

    if partTwo:
        # special case, all of them are J's
        if not cs:
            cs = [0]
        # if sum of counted cards is < 5, is becase there are (5 - sum) J's
        cs[0] += 5 - sum(cs)

    # five of a kind
    if cs[0] == 5:
        return 7
    # four of a kind
    elif cs[0] == 4:
        return 6
    # full house
    elif cs[0] == 3 and cs[1] == 2:
        return 5
    # three of a kind
    elif cs[0] == 3:
        return 4
    # two pairs
    elif cs[0] == 2 and cs[1] == 2:
        return 3
    # one pair
    elif cs[0] == 2:
        return 2
    # high card
    return 1

def compare_hands(hand1, hand2):
    # compare score
    if hand1[2] != hand2[2]:
        return hand1[2] - hand2[2]
    # compare cards in order
    for i in range(len(hand1[0])):
        if C_VALUES[hand1[0][i]] != C_VALUES[hand2[0][i]]:
            return C_VALUES[hand1[0][i]] - C_VALUES[hand2[0][i]]
    return 0

# Part 1
total = sum([
    (i+1) * hand[1]
    for i, hand in enumerate(sorted([
        (hand, int(bid_str), hand_score(hand))
        for hand, bid_str in inputs
    ], key=cmp_to_key(compare_hands)))
])

print("Part 1: {}".format(total))

# Part 2
C_VALUES['J'] = 0 # remove value of J

total = sum([
    (i+1) * hand[1]
    for i, hand in enumerate(sorted([
        (hand, int(bid_str), hand_score(hand, partTwo=True))
        for hand, bid_str in inputs
    ], key=cmp_to_key(compare_hands)))
])

print("Part 2: {}".format(total))
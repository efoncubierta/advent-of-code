with open("input.txt", "r") as file:
    inputs = file.read().split(",")

def hash_str(str):
    t = 0
    for c in str:
        t += ord(c)
        t *= 17
        t %= 256
    return t

# Part 1
t = sum([
    hash_str(input)
    for input in inputs
])
print("Part 1: {}".format(t))

# Part 2
boxes = []
for i in range(0, 256):
    boxes.append([])

for input in inputs:
    # extract label and operation
    op_i = [i for i,c in enumerate(input) if c in '=-'][0]
    op = input[op_i]
    label = input[0:op_i]

    # calculate box for label
    box_i = hash_str(label)

    # find current slot of label if exists
    slot_ii = [i for i, v in enumerate(boxes[box_i]) if v[0] == label]
    slot = slot_ii[0] if slot_ii else -1

    if op == '=':
        # extract focal length
        f_length = int(input[op_i+1:])
        if slot > -1:
            # replace
            boxes[box_i][slot] = [label, f_length]
        else:
            # add
            boxes[box_i].append([label, f_length])
    elif op == '-':
        if slot > -1:
            # remove
            boxes[box_i] = boxes[box_i][:slot] + boxes[box_i][slot+1:]

total = sum([
    (i+1) * (j+1) * kv[1]
    for i, box in enumerate(boxes)
    for j, kv in enumerate(box)
])
print("Part 2: {}".format(total))
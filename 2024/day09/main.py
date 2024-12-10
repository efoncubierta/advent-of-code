with open("input.txt", "r") as f:
    input = [int(n) for n in f.read()]

FILES, SIZES, FREE = [], {}, []
id = -1
for i in range(0, len(input), 2):
    id += 1
    FILES += [id] * input[i]
    if (i+1 < len(input)):
        FREE.append((len(FILES), input[i+1]))
        FILES += [-1] * input[i+1]# free space is -1
    SIZES[id] = input[i]


def sort1(files):
    i, j = 0, len(files) - 1
    while i < j:
        # find forward next free space
        if files[i] < 0:
            # find backwards next file to move
            while files[j] < 0:
                j -= 1
            # move
            files[i], files[j] = files[j], -1
            j -= 1
        i += 1

def sort2(files):
    file_i = len(files) - 1
    while file_i > 0:
        # find next file index from the right
        if files[file_i] < 0:
            file_i -= 1
            continue

        file_s = SIZES[files[file_i]]
        file_i = file_i - file_s + 1
        
        # find free space to move the file
        for space_i, space in enumerate(FREE):
            # no space towards the left
            if space[0] > file_i:
                break
            # skip if not enough space
            if space[1] < file_s:
                continue
            
            # move file
            for jj in range(file_s):
                files[space[0]+jj] = files[file_i+jj]
                files[file_i+jj] = -1
            
            # recalculate space
            FREE[space_i] = (space[0]+file_s, space[1]-file_s)
            break
        
        # move backwards to find the next file
        file_i -= 1

def checksum(files):
    return sum([(i * int(files[i])) for i in range(len(files)) if files[i] >= 0])

files = FILES.copy()
sort1(files)
print("Part 1: {}".format(checksum(files)))

files = FILES.copy()
sort2(files)
print("Part 2: {}".format(checksum(files)))
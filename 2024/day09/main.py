with open("input.txt", "r") as f:
    input = [int(n) for n in f.read()]

FILES, SIZES = [], {}
id = -1
for i in range(0, len(input), 2):
    id += 1
    FILES += [id] * input[i]
    FILES += [-1] * input[i+1] if i+1 < len(input) else []
    SIZES[id] = input[i]

def sort1(files):
    i, j = 0, len(files) - 1
    while i < j:
        if files[i] < 0:
            while files[j] < 0:
                j -= 1
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
        
        space_i = 0
        while space_i < file_i:
            # find next free space from the left
            while files[space_i] >= 0:
                space_i += 1
                continue
            
            space_s = 1
            while (space_i + space_s) < len(files) and files[space_i + space_s] < 0:
                space_s += 1
            
            # move if file fits in free space
            if space_i < file_i and space_s >= file_s:
                for jj in range(file_s):
                    files[space_i+jj] = files[file_i+jj]
                    files[file_i+jj] = -1
                break
            
            # if not, move forward to find next free space
            space_i += space_s
        
        # move backwards to find the next file
        file_i -= 1

def checksum(files):
    sum = 0
    for i in range(len(files)):
        if files[i] < 0:
            continue
        sum += (i * int(files[i]))
    return sum

files = FILES.copy()
sort1(files)
print("Part 1: {}".format(checksum(files)))

files = FILES.copy()
sort2(files)
print("Part 2: {}".format(checksum(files)))
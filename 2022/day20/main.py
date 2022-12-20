with open("input.txt", "r") as f:
    values = [
        (i, int(v)) # same value can appear multiple times, add index
        for i, v in enumerate(f.read().splitlines())
    ]

def decrypt(key, n):
    # decrypted values
    d_values = [(i[0], key*i[1]) for i in values]
    # sorted values
    s_values = d_values.copy()
    for _ in range(n):
        for i in range(len(d_values)):
            vi = s_values.index(d_values[i])
            v = s_values.pop(vi)
            vi = (vi + v[1]) % len(s_values)
            # index correction
            # according to instructions, values at 0 index are moved to the tail
            vi = len(s_values) if vi == 0 else vi
            s_values.insert(vi, v)

    zi = [i for i, v in enumerate(s_values) if v[1] == 0][0]
    total = 0
    for i in range(1000, 3001, 1000):
        total += s_values[(zi + i) % len(s_values)][1]

    return total

print("Part #1: {}".format(decrypt(1, 1)))
print("Part #2: {}".format(decrypt(811589153, 10)))

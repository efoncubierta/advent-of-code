import math

with open("input.txt", "r") as f:
    inputs = [[
        [int(n.strip()) for n in k[0].split(":")[1].split(",")],
        k[1].split("=")[1].strip().split(" "),
        [
            int(k[2].split(" ")[-1]),
            int(k[3].split(" ")[-1]),
            int(k[4].split(" ")[-1])
        ]
    ] for k in [j.split("\n")[1:] for j in [i for i in f.read().split("\n\n")]]]

stats = [0] * len(inputs)

def calculate(n, adjustFunc):
    for _ in range(0, n):
        for i, input in enumerate(inputs):
            for item in input[0]:
                if input[1][1] == "+":
                    item += item if input[1][2] == "old" else int(input[1][2])
                else:
                    item *= item if input[1][2] == "old" else int(input[1][2])

                item = adjustFunc(item)

                if (item % input[2][0]) == 0:
                    inputs[input[2][1]][0].append(item)
                else:
                    inputs[input[2][2]][0].append(item)

                input[0] = input[0][1:]
                stats[i] += 1
    return math.prod(sorted(stats)[-2:])

# least common multiple of all "divisible by"
lcm = math.lcm(*[i[2][0] for i in inputs])

print("Monkey business #1: {}".format(calculate(20, lambda x: math.floor(x/3))))
print("Monkey business #2: {}".format(calculate(10000, lambda x: x % lcm)))

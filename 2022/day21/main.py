from sympy.solvers import solve
from sympy import Symbol

x = Symbol('x')

with open("input.txt", "r") as f:
    inputs = {
        i[0][:-1]: (int(i[1]),) if len(i) == 2 else (i[1], i[2], i[3])
        for i in [
            v.split(" ")
            for v in f.read().splitlines()
        ]
    }


def calc(m, isPart2=False):
    if isPart2 and m == "root":
        return solve(calc(inputs[m][0], isPart2) - calc(inputs[m][2], isPart2), x)[0]

    if isPart2 and m == "humn":
        return x

    if len(inputs[m]) == 1:
        return inputs[m][0]

    if inputs[m][1] == "+":
        return calc(inputs[m][0], isPart2) + calc(inputs[m][2], isPart2)

    if inputs[m][1] == "-":
        return calc(inputs[m][0], isPart2) - calc(inputs[m][2], isPart2)

    if inputs[m][1] == "*":
        return calc(inputs[m][0], isPart2) * calc(inputs[m][2], isPart2)

    if inputs[m][1] == "/":
        return calc(inputs[m][0], isPart2) / calc(inputs[m][2], isPart2)


print("Part #1: {}".format(int(calc("root"))))

print("Part #2: {}".format(int(calc("root", True))))

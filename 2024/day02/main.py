with open("input.txt", "r") as f:
    inputs = [[int(a) for a in input.split()] for input in f.read().split("\n")]

def check_report(report):
    asc = report[0] < report[1]
    valid = True
    for i in range(0, len(report) - 1):
        d = report[i] - report[i + 1]
        if asc and (d > -1 or d < -3):
            valid = False
        elif not asc and (d > 3 or d < 1):
            valid = False
    return valid

c = 0
for report in inputs:
    if check_report(report):
        c += 1

print("Part 1: {}".format(c))

c = 0
for report in inputs:
    if check_report(report):
        c += 1
    else:
        for i in range(0, len(report)):
            if check_report(report[:i] + report[i+1:]):
                c += 1
                break

print("Part 2: {}".format(c))
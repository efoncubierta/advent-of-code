with open("input.txt", "r") as f:
    inputs = f.read().split("\n\n")

calories = list(map(lambda x: sum(map(lambda n: int(n), x.splitlines())), input))
calories.sort(reverse=True)

print("Top 1 total calories = {}".format(calories[0]))
print("Top 3 total calories = {}".format(sum(calories[0:3])))

with open("input.txt", "r") as f:
    inputs = [i.split(" ") for i in f.read().splitlines()]

# Part 1
X = 1
cycle = 0
strength = 0

def refreshStrength(cycles):
  global cycle, strength
  for _ in range(0, cycles):
    cycle += 1
    if (cycle - 20) % 40 == 0:
      strength += X * cycle

for input in inputs:
  if input[0] == "noop":
    refreshStrength(1)
  else:
    refreshStrength(2)
    X += int(input[1])

print("Total signal strength: {}".format(strength))

# Part 2
X = 1
cycle = 0
screen = list("."*240)

def refreshScreen(cycles):
  global cycle
  for _ in range(0, cycles):
    if (cycle % 40) in range(X-1, X+2, 1):
      screen[cycle] = "#"
    cycle += 1

for input in inputs:
  if input[0] == "noop":
    refreshScreen(1)
  else:
    refreshScreen(2)
    X += int(input[1])

for i in range(0, 240, 40):
  print("".join(screen[i:i+40]))
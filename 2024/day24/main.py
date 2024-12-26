import re
from collections import defaultdict
from itertools import combinations

with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

I_STATE = {}
GATES = []

for l in input[0].splitlines():
    w, v = l.split(': ')
    I_STATE[w] = int(v)
    
for l in input[1].splitlines():
    m = re.match(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", l)
    if m:
        GATES.append(m.groups())

def simulate(state, gates):
    resolved = False
    while not resolved:
        resolved = True
        for w1, op, w2, wo in gates:
            if state[wo] is None:
                if state[w1] is not None and state[w2] is not None:
                    if op == 'AND':
                        state[wo] = state[w1] & state[w2]
                    elif op == 'OR':
                        state[wo] = state[w1] | state[w2]
                    elif op == 'XOR':
                        state[wo] = state[w1] ^ state[w2]
                else:
                    resolved = False
    return state

STATE = defaultdict(lambda: None, I_STATE)
STATE = simulate(STATE, GATES)

binary_str = ''.join(map(str, reversed([STATE[k] for k in sorted(STATE.keys()) if k.startswith('z')])))
print("Part 1:", int(binary_str, 2))
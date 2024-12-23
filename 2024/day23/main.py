from collections import defaultdict

with open("input.txt", "r") as f:
    input = [i.split("-") for i in f.read().split("\n")]

graph = defaultdict(set)
for (a, b) in input:
    graph[a].add(b)
    graph[b].add(a)

conns = [(a, b, c)
    for a in graph
    for b in graph[a]
    for c in graph[b]
    if c in graph[a] and a < b < c]

print("Part 1:", len([s for s in conns if any(n.startswith('t') for n in s)]))

# Bron-Kerbosch
def find(graph, r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
    else:
        for v in list(p):
            find(graph, r | {v}, p & graph[v], x & graph[v], cliques)
            p.remove(v)
            x.add(v)

cliques = []
find(graph, set(), set(graph.keys()), set(), cliques)
print("Part 2:", ",".join(sorted(max(cliques, key=len))))
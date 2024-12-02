import networkx as nx

with open("input.txt", "r") as file:
    inputs = [
        input.split(": ")
        for input in file.read().split("\n")
    ]
    G = nx.Graph()
    for i in inputs:
        ts = i[1].split(" ")
        for t in ts:
            G.add_edge(i[0], t)

G.remove_edges_from(nx.minimum_edge_cut(G))
graph = list(nx.connected_components(G))

total = 1
for i in graph:
    total *= len(i)
print("Part 1: ", total)
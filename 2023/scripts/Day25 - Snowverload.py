from functools import reduce
import networkx as nx

# inFile = open('../inputs/Day25.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2023/inputs/Day25.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 25 - Snowverload')

# Part 1
graph = nx.Graph()

for line in lines:
	l, rs = line.split(': ')
	for r in rs.split(' '):
		graph.add_edge(l, r)

cut_edges = nx.minimum_edge_cut(graph)
graph.remove_edges_from(cut_edges)

subgraphs = list(graph.subgraph(c) for c in nx.connected_components(graph))
sg_size = reduce(lambda acc, sg: acc * len(sg), subgraphs, 1)

print(f"Part 1: {sg_size}")

# Part 2
# Pushed the Big Red Button
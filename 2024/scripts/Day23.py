from utils import *
from datetime import datetime
import networkx as nx

def part_1(graph):
	connected = [list(triangle) for triangle in nx.enumerate_all_cliques(graph) if len(triangle) == 3]
	return sum(any(c.startswith('t') for c in conn) for conn in connected)

def part_2(graph):
	return ','.join(sorted(max(nx.find_cliques(graph), key=len)))

def main(year, day):
	print(f'Day {day} - LAN Party')

	input = get_input(year, day, test=False)
	graph = nx.Graph()

	for line in input:
		src, dst = line.split('-')
		graph.add_edge(src, dst)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(graph)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(graph)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
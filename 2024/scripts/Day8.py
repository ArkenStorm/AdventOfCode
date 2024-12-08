from utils import *
from datetime import datetime
from collections import defaultdict
import numpy as np

def in_bounds(grid, x, y):
	return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def part_1(grid, node_coords):
    antinode_coords = set()

    for nodes in (node_coords.values()):
        for (a, b) in nodes:
            diff = (b[0] - a[0], b[1] - a[1])
            neighbors = [(a[0] - diff[0], a[1] - diff[1]), (b[0] + diff[0], b[1] + diff[1])]

            antinode_coords.update(coord for coord in neighbors if in_bounds(grid, *coord))

    return len(antinode_coords)

def add_vector_nodes(start, step, coords, grid):
	curr = start
	while in_bounds(grid, *curr):
		coords.add(curr)
		curr = (curr[0] + step[0], curr[1] + step[1])

def part_2(grid, node_coords):
	antinode_coords = set()

	for nodes in (node_coords.values()):
		for pair in nodes:
			diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
			add_vector_nodes(pair[0], (-diff[0], -diff[1]), antinode_coords, grid)
			add_vector_nodes(pair[1], diff, antinode_coords, grid)
	return len(antinode_coords)

def main(year, day):
	print(f'Day {day} - Resonant Collinearity')

	input = get_input(year, day, type='grid', test=False)

	grid = np.array(input)
	node_coords = defaultdict(list)

	for i in range(grid.shape[0]):
		for j in range(grid.shape[1]):
			if input[i][j] != '.':
				node_coords[input[i][j]].append((i, j))

	for key, nodes in node_coords.items():
		node_coords[key] = [sorted((a, b)) for idx, a in enumerate(nodes) for b in nodes[idx + 1:]]

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid, node_coords)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid, node_coords)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
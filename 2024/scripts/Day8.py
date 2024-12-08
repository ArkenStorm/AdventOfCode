from utils import *
from datetime import datetime
from collections import defaultdict
import numpy as np

def in_bounds(grid, x, y):
	return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def part_1(grid, node_coords):
	antinode_coords = set()

	for key in node_coords:
		coord_pairs = [sorted((a, b)) for idx, a in enumerate(node_coords[key]) for b in node_coords[key][idx + 1:]]
		for pair in coord_pairs:
			diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
			a1 = (pair[0][0] - diff[0], pair[0][1] - diff[1])
			a2 = (pair[1][0] + diff[0], pair[1][1] + diff[1])
			if in_bounds(grid, *a1):
				antinode_coords.add(a1)
			if in_bounds(grid, *a2):
				antinode_coords.add(a2)
	return len(antinode_coords)

def part_2(grid, node_coords):
	antinode_coords = set()

	for key in node_coords:
		coord_pairs = [sorted((a, b)) for idx, a in enumerate(node_coords[key]) for b in node_coords[key][idx + 1:]]
		for pair in coord_pairs:
			diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])

			curr = pair[0]
			while True:
				if not in_bounds(grid, *curr):
					break
				antinode_coords.add(curr)
				curr = (curr[0] - diff[0], curr[1] - diff[1])

			curr = pair[1]
			while True:
				if not in_bounds(grid, *curr):
					break
				antinode_coords.add(curr)
				curr = (curr[0] + diff[0], curr[1] + diff[1])

	return len(antinode_coords)

def main(year, day):
	print(f'Day {day} - Title')

	input = get_input(year, day, type='grid', test=False)

	node_coords = defaultdict(list)
	grid = np.array(input)

	for i in range(grid.shape[0]):
		for j in range(grid.shape[1]):
			if input[i][j] != '.':
				node_coords[input[i][j]].append((i, j))

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid, node_coords)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid, node_coords)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
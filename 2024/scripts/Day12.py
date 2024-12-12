from utils import *
from datetime import datetime
import numpy as np
from itertools import combinations

visited = set()

def flood_fill(grid, i, j, p2):
	if (i, j) in visited:
		return 0, 0
	visited.add((i, j))
	coords = list(filter(lambda x: grid[i,j] == grid[x[0], x[1]], get_bounded_4_neighbors(grid, i, j)))
	perimeter = 0 if p2 else 4 - len(coords)
	if len(coords) == 0:
		return 1, 4
	if p2:
		if len(coords) == 1:
			perimeter = 2
		else:
			check_coords = list(filter(lambda c: c != (i, j), [(x1 + x2 - i, y1 + y2 - j) for (x1, y1), (x2, y2) in combinations(coords, 2)]))
			if len(coords) == 2 and len(check_coords) > 0: # "L" shape
				perimeter = 1
			perimeter += sum(1 for coord in check_coords if grid[coord] != grid[i, j])
	area = 1
	for coord in list(filter(lambda x: x not in visited, coords)):
		a, p = flood_fill(grid, *coord, p2)
		area += a
		perimeter += p

	return area, perimeter

def solve(grid, p2=False):
	total = 0
	for i, j in np.ndindex(grid.shape):
		if (i, j) not in visited:
			area, perimeter = flood_fill(grid, i, j, p2)
			total += area * perimeter
	return total

def part_1(grid):
	return solve(grid)

def part_2(grid):
	return solve(grid, p2=True)

def main(year, day):
	print(f'Day {day} - Garden Groups')

	grid = get_input(year, day, type='np_grid', test=False)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid)}')
	p1_end = datetime.now()

	visited.clear()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
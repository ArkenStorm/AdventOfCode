from utils import *
from datetime import datetime
import numpy as np

visited = set()

def get_perimeter(grid, coords, p2):
	if p2:
		pass
	else:
		return 4 - len(coords)

def flood_fill(grid, i, j, p2=False):
	if (i, j) in visited:
		return 0, 0
	visited.add((i, j))
	perimeter = 0
	coords = list(filter(lambda x: grid[i,j] == grid[x[0], x[1]], get_bounded_4_neighbors(grid, i, j)))
	if len(coords) == 0:
		return 1, 4
	else:
		perimeter = 4 - len(coords)
	coords = list(filter(lambda x: x not in visited, coords))
	area = 1
	for coord in coords:
		a, p = flood_fill(grid, *coord, p2)
		area += a
		perimeter += p

	return area, perimeter

def part_1(grid):
	total = 0
	for i, j in np.ndindex(grid.shape):
		if (i, j) not in visited:
			area, perimeter = flood_fill(grid, i, j)
			total += area * perimeter
	return total

def part_2(grid):
	total = 0
	for i, j in np.ndindex(grid.shape):
		if (i, j) not in visited:
			# Probably not going to work out like this, but it might
			area, perimeter = flood_fill(grid, i, j, True)
			total += area * perimeter
	return total

def main(year, day):
	print(f'Day {day} - Garden Groups')

	grid = get_input(year, day, type='grid', test=True)
	grid = np.array(grid)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
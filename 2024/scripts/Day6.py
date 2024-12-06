from utils import *
from datetime import datetime
import numpy as np

dirs = { 'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1) }
turns = { 'n': 'e', 'e': 's', 's': 'w', 'w': 'n' }

def in_bounds(grid, x, y):
	return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

def get_next_coord(x, y, dir):
	return x + dirs[dir][0], y + dirs[dir][1]

def part_1(grid, start):
	x, y = start[0], start[1]
	dir = 'n'
	unique = 0

	while in_bounds(grid, x, y):
		if grid[x,y] != 'X':
			grid[x, y] = 'X'
			unique += 1
		next_x, next_y = get_next_coord(x, y, dir)
		if not in_bounds(grid, next_x, next_y):
			break
		if grid[next_x, next_y] == '#':
			dir = turns[dir]
		x, y = get_next_coord(x, y, dir)
	return unique

def follow_path(grid, start, dir):
	x, y = start[0], start[1]
	seen = set()
	seen.add((x, y, dir))

	while in_bounds(grid, x, y):
		if not in_bounds(grid, *get_next_coord(x, y, dir)):
			break
		while grid[*get_next_coord(x, y, dir)] == '#':
			dir = turns[dir]
		seen.add((x, y, dir))
		x, y = get_next_coord(x, y, dir)
		if (x, y, dir) in seen:
			return True
	return False

def part_2(grid, start):
	x, y = start[0], start[1]
	dir = 'n'
	block_options = 0
	test_obstacles = set()

	while in_bounds(grid, x, y):
		next_x, next_y = get_next_coord(x, y, dir)
		if not in_bounds(grid, next_x, next_y):
			break
		prev = grid[next_x, next_y]
		grid[next_x, next_y] = '#'
		if (next_x, next_y) not in test_obstacles and follow_path(grid, start, 'n'):
			block_options += 1
		test_obstacles.add((next_x, next_y))
		grid[next_x, next_y] = prev
		if prev == '#':
			dir = turns[dir]
		else:
			x, y = get_next_coord(x, y, dir)

	return block_options


def main(year, day):
	print(f'Day {day} - Guard Gallivant')

	input = get_input(year, day, type='grid', test=False)
	grid = np.array(input)

	start = np.where(grid == '^')
	start = (start[0][0], start[1][0])

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid, start)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid, start)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
from utils import *
from datetime import datetime
import numpy as np

dirs = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }

# los == line of sight
def get_los_slice(grid, x, y, move):
	if move == '^':
		return grid[0:x+1, y][::-1]
	elif move == 'v':
		return grid[x:, y]
	elif move == '<':
		return grid[x, 0:y+1][::-1]
	elif move == '>':
		return grid[x, y:]

def part_1(grid, movements):
	start = np.where(grid == '@')
	x, y = start[0][0], start[1][0]
	for move in movements:
		dx, dy = dirs[move]
		los = get_los_slice(grid, x, y, move)

		first_wall = np.where(los == '#')[0][0]
		first_space = np.where(los == '.')[0]
		if len(first_space) == 0 or (first_space := first_space[0]) > first_wall:
			continue
		new_positions = np.roll(los[:first_space + 1], 1)
		if move == '^':
			grid[x - first_space:x + 1, y] = new_positions[::-1]
		elif move == '>':
			grid[x, y:y + first_space + 1] = new_positions
		elif move == 'v':
			grid[x:x + first_space + 1, y] = new_positions
		elif move == '<':
			grid[x, y - first_space:y + 1] = new_positions[::-1]
		x, y = x + dx, y + dy

	return sum(100 * x + y for x, y in zip(*np.where(grid == 'O')))

def part_2(grid, movements):
	# update grid
	new_grid = [[] for _ in range(grid.shape[0])]
	for i, j in np.ndindex(grid.shape):
		if grid[i, j] == '#':
			new_grid[i] += ['#', '#']
		elif grid[i, j] == 'O':
			new_grid[i] += ['[', ']']
		elif grid[i, j] == '.':
			new_grid[i] += ['.', '.']
		elif grid[i, j] == '@':
			new_grid[i] += ['@', ',']
	grid = new_grid

def main(year, day):
	print(f'Day {day} - Warehouse Woes')

	input = get_input(year, day, type='other', test=True)

	grid, movements = input.split('\n\n')
	grid = np.array([list(x) for x in grid.split('\n')])
	movements = ''.join(movements.split('\n'))

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid, movements)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid, movements)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
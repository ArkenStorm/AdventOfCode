from utils import *
from datetime import datetime
import numpy as np

dirs = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }

# los == line of sight
def get_los_slice(grid, x, y, move):
	if move == '^': return grid[:x+1, y][::-1], [(i, y) for i in range(x + 1)][::-1]
	elif move == 'v': return grid[x:, y], [(i, y) for i in range(x, len(grid))]
	elif move == '<': return grid[x, :y+1][::-1], [(x, j) for j in range(y + 1)][::-1]
	elif move == '>': return grid[x, y:], [(x, j) for j in range(y, len(grid[0]))]

def get_new_positions(grid, x, y, move):
	los, coords = get_los_slice(grid, x, y, move)

	first_wall = np.where(los == '#')[0][0]
	first_space = np.where(los == '.')[0]
	# if there are no spaces or the first space is after the first wall
	if len(first_space) == 0 or (first_space := first_space[0]) > first_wall:
		return None, None, None
	return np.roll(los[:first_space + 1], 1), first_space, set(coords[:first_space + 1])

def get_box_chain(grid, x, y, move, checked):
	new_positions, first_space, covered_coords = get_new_positions(grid, x, y, move)
	if new_positions is None:
		return [None]
	dx, dy = dirs[move]
	next_x, next_y = x + dx, y + dy
	box_chain = [(new_positions, first_space, (x, y))] if (x, y) not in checked else []
	checked.update(covered_coords)
	if grid[next_x + dx, next_y + dy] in '[]' and grid[next_x, next_y] != '.':
		check = get_box_chain(grid, next_x, next_y, move, checked)
		if None in check:
			return [None]
		box_chain += check
	if grid[next_x, next_y] == '[':
		box_chain += get_box_chain(grid, next_x, next_y + 1, move, checked)
	elif grid[next_x, next_y] == ']':
		box_chain += get_box_chain(grid, next_x, next_y - 1, move, checked)
	return box_chain

def update_positions(grid, x, y, move, new_positions, first_space):
	if move == '^': grid[x - first_space:x + 1, y] = new_positions[::-1]
	elif move == '>': grid[x, y:y + first_space + 1] = new_positions
	elif move == 'v': grid[x:x + first_space + 1, y] = new_positions
	elif move == '<': grid[x, y - first_space:y + 1] = new_positions[::-1]

def print_grid(grid, move=None, step=0):
	print('\nInitial State - Step 0:' if move is None else f'Move {move} - Step {step}:')
	for row in grid:
		print(''.join(row))
	print('\n\n')

def update_grid(grid, x, y, movements, p2=False, debug=False):
	step = 1
	for move in movements:
		dx, dy = dirs[move]
		next_x, next_y = x + dx, y + dy
		new_positions, first_space, _ = get_new_positions(grid, x, y, move)
		if new_positions is None:
			if debug: print_grid(grid, move, step)
			step += 1
			continue
		if move in '<>' or grid[next_x, next_y] == '.' or not p2:
			update_positions(grid, x, y, move, new_positions, first_space)
			x, y = next_x, next_y
		else:
			affected = get_box_chain(grid, x, y, move, set())
			if None not in affected:
				for nps, fs, (sx, sy) in affected:
					update_positions(grid, sx, sy, move, nps, fs)
				x, y = next_x, next_y
		if debug: print_grid(grid, move, step)
		step += 1

def part_1(grid, movements):
	x, y = list(zip(*np.where(grid == '@')))[0]
	update_grid(grid, x, y, movements)
	return sum(100 * x + y for x, y in zip(*np.where(grid == 'O')))

def part_2(grid, movements, debug=False):
	replacements = {'#': ['#', '#'], 'O': ['[', ']'], '.': ['.', '.'], '@': ['@', '.']}
	grid = np.array([[replacement for j in row for replacement in replacements[j]] for row in grid])
	x, y = list(zip(*np.where(grid == '@')))[0]

	if debug: print_grid(grid)
	update_grid(grid, x, y, movements, p2=True, debug=debug)

	return sum(100 * x + y for x, y in zip(*np.where(grid == '[')))

def main(year, day):
	print(f'Day {day} - Warehouse Woes')

	input = get_input(year, day, type='other', test=False)

	grid, movements = input.split('\n\n')
	grid = np.array([list(x) for x in grid.split('\n')])
	movements = ''.join(movements.split('\n'))

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid.copy(), movements)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid, movements, debug=False)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
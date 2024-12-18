import numpy as np

def get_input(year, day_num, type='default', test=False):
	in_file = open(f"{year}/inputs/{'test' if test else f'Day{day_num}'}.txt", 'r')
	content = in_file.read()
	if type == 'default':
		return content.splitlines()
	elif type == 'grid':
		return [list(line) for line in content.splitlines()]
	elif type == 'np_grid':
		return np.array([list(line) for line in content.splitlines()])
	else:
		return content

deltas_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
deltas_8 = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def apply_deltas_4(i, j):
	return [(i + dx, j + dy) for dx, dy in deltas_4]

def apply_deltas_8(i, j):
	return [(i + dx, j + dy) for dx, dy in deltas_8]

# coords is an array of tuples
def get_bounded_coords(grid, coords):
	return [x for x in coords if 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0])]

def get_bounded_4_neighbors(grid, i, j):
	return get_bounded_coords(grid, apply_deltas_4(i, j))

def get_bounded_8_neighbors(grid, i, j):
	return get_bounded_coords(grid, apply_deltas_8(i, j))
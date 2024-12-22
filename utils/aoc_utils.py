import numpy as np
from time import perf_counter_ns

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

def apply_deltas_4(x, y):
	return [(x + dx, y + dy) for dx, dy in deltas_4]

def apply_deltas_8(x, y):
	return [(x + dx, y + dy) for dx, dy in deltas_8]

# coords is an array of tuples
def get_bounded_coords(grid, coords):
	return [x for x in coords if 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0])]

def get_bounded_4_neighbors(grid, x, y):
	return get_bounded_coords(grid, apply_deltas_4(x, y))

def get_bounded_8_neighbors(grid, x, y):
	return get_bounded_coords(grid, apply_deltas_8(x, y))

def benchmark(func):
	def wrapper(*args, **kwargs):
		start = perf_counter_ns()
		result = func(*args, **kwargs)
		end = perf_counter_ns() - start

		hours, remainder = divmod(end, 3_600_000_000_000)
		minutes, remainder = divmod(remainder, 60_000_000_000)
		seconds, remainder = divmod(remainder, 1_000_000_000)
		milliseconds, remainder = divmod(remainder, 1_000_000)
		microseconds, nanoseconds = divmod(remainder, 1_000)

		formatted_time = f'{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}.{microseconds:03}.{nanoseconds:03}'
		print(f'{func.__name__}: {formatted_time}')
		return result
	return wrapper
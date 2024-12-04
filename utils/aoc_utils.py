def get_input(year, day_num, type='default', test=False):
	inFile = open(f"{year}/inputs/{'test' if test else f'Day{day_num}'}.txt", 'r')
	if type == 'default':
		return inFile.read().splitlines()
	elif type == 'grid':
		return [list(line) for line in inFile.read().splitlines()]
	else:
		return inFile.read()

# coords is an array of tuples
def get_bounded_coords(grid, coords):
	return [x for x in coords if 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0])]

def get_bounded_4_neighbors(grid, i, j):
	return get_bounded_coords(grid, [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)])

def get_bounded_8_neighbors(grid, i, j):
	return get_bounded_coords(grid, [
		(i - 1, j - 1),
		(i - 1, j),
		(i - 1, j + 1),
		(i, j - 1),
		(i, j + 1),
		(i + 1, j - 1),
		(i + 1, j),
		(i + 1, j + 1)
	])
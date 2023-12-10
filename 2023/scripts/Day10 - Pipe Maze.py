import numpy as np
from matplotlib.path import Path
from functools import reduce

inFile = open('../inputs/Day10.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day10.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 10 - Pipe Maze')

grid = np.array([list(line) for line in lines])

# Part 1

start = np.argwhere(grid == 'S')
steps, pos = 0, tuple(start[0])
loop = [pos]

def get_possible_next(tile, x, y):
	n, e, s, w = (x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)
	tile_map = { '|': (n, s), '-': (w, e), 'L': (n, e), 'J': (n, w), '7': (s, w), 'F': (s, e) }
	if tile == 'S':
		if grid[x - 1, y] in '|7F':
			return n
		elif grid[x + 1, y] in '|LJ':
			return s
		elif grid[x, y + 1] in '-J7':
			return e
		elif grid[x, y - 1] in '-LF':
			return w
	else:
		return tile_map[tile]


pos = get_possible_next('S', *pos)
curr_tile = grid[pos[0], pos[1]]

while curr_tile != 'S':
	loop.append(pos)
	first, second = get_possible_next(curr_tile, *pos)
	pos = first if loop[-2] != first else second
	curr_tile = grid[pos[0], pos[1]]

print(f"Part 1: {len(loop) // 2}")

# Part 2
enclosed_points = 0
polygon = Path(loop)

reductor = lambda acc, coords: acc + 1 if coords not in loop and polygon.contains_point(coords) else acc
enclosed_points = reduce(reductor, ((x, y) for x in range(len(lines)) for y in range(len(lines[0]))), 0)

print(f"Part 2: {enclosed_points}")
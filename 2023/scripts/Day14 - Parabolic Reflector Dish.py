import numpy as np
from functools import reduce
from itertools import chain

# inFile = open('../inputs/Day14.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2023/inputs/Day14.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 14 - Parabolic Reflector Dish')

platform = np.array([list(line) for line in lines])

def grid_str(grid: np.ndarray):
	return '\n'.join([''.join(r) for r in grid.tolist()])

states = { grid_str(platform): 0 }  # grid state: iteration

def tilt(grid):
	for i in range(len(lines[0])):
		col = ''.join(chain.from_iterable(grid[:,i:i+1])).split('#')
		for j in range(len(col)):
			col[j] = ''.join(sorted(col[j])[::-1])
		sorted_col = '#'.join(col)	
		grid[:,i:i+1] = np.array(list([r] for r in sorted_col))
	return grid

def get_load(grid):
	return sum(len(grid) - i if grid[i][j] == 'O' else 0 for j in range(len(grid[0])) for i in range(len(grid)))

# Part 1
tilt(platform)
total = get_load(platform)

print(f"Part 1: {total}")

# Part 2
def cycle(grid):
	for _ in range(4):
		tilt(grid)
		grid = np.rot90(grid, axes=(1,0))
	return grid

cycle_start, period = 0, 0
for i in range(1, 1000000000):
	platform = cycle(platform)
	total = get_load(platform)
	key = grid_str(platform)
	if key in states:
		cycle_start = states[key]
		period = i - cycle_start
		break
	else:
		states[key] = i

final = list(states.keys())[list(states.values()).index(cycle_start + (1000000000 - cycle_start) % period)].split()
platform = np.array([list(r) for r in final])

total = get_load(platform)

print(f"Part 2: {total}")
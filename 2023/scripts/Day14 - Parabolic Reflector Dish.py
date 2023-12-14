import numpy as np
from functools import reduce
from itertools import chain

# inFile = open('../inputs/Day14.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day14.txt')
inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

platform = np.array([list(line) for line in lines])

print('Day 14 - Parabolic Reflector Dish')

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
new_grid = tilt(platform)
total = get_load(new_grid)

print(f"Part 1: {total}")

# Part 2
states = { np.array2string(platform): 0 }  # grid state: iteration
new_grid = platform
cycle_start, period = 0, 0
for i in range(1000000000):
	for j in range(4):
		new_grid = tilt(np.rot90(new_grid, axes=(1,0)))
	total = get_load(new_grid)
	grid_str = np.array2string(new_grid)
	if grid_str in states:
		cycle_start = states[grid_str]
		period = i - cycle_start - 1
		break
	else:
		states[grid_str] = i

for i in range(cycle_start + (1000000000 - cycle_start) % period):
	for j in range(4):
		new_grid = tilt(np.rot90(new_grid, axes=(1,0)))

total = get_load(new_grid)

print(f"Part 2: {total}")
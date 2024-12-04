from utils import *
from datetime import datetime

def find_xmas(grid, i, j):
	# check all 8 directions, unless bounds don't make sense
	found = 0
	directions = [
		[(i - 1, j), (i - 2, j), (i - 3, j)], # up
		[(i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)], # up-right
		[(i, j + 1), (i, j + 2), (i, j + 3)], # right
		[(i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)], # down-right
		[(i + 1, j), (i + 2, j), (i + 3, j)], # down
		[(i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)], # down-left
		[(i, j - 1), (i, j - 2), (i, j - 3)], # left
		[(i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)] # up-left
	]

	bound_filter = lambda arr: all([0 <= x < len(grid) and 0 <= y < len(grid[0]) for x, y in arr])

	for d in filter(bound_filter, directions):
		if grid[d[0][0]][d[0][1]] == 'M' and grid[d[1][0]][d[1][1]] == 'A' and grid[d[2][0]][d[2][1]] == 'S':
			found += 1
	return found

def part_1(input):
	return sum(find_xmas(input, i, j) for i in range(len(input)) for j in range(len(input[i])) if input[i][j] == 'X')

def find_x_mas(grid, i, j):
	tlbr = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1] # top left bottom right
	bltr = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1] # bottom left top right
	return tlbr in ['MAS', 'SAM'] and bltr in ['MAS', 'SAM']

def part_2(input):
    return sum(find_x_mas(input, i, j) for i in range(1, len(input) - 1) for j in range(1, len(input[i]) - 1) if input[i][j] == 'A')

def main(year, day):
	print(f'Day {day} - Ceres Search')

	input = get_input(year, day, type='grid', test=False)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(input)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(input)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
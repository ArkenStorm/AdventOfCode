from utils import *
from datetime import datetime

def dfs(grid, i, j, seen):
	seen.add((i, j))
	if grid[i][j] == '9':
		return 1

	score = 0
	verify = lambda x: x not in seen and int(grid[x[0]][x[1]]) == int(grid[i][j]) + 1
	coords = filter(verify, get_bounded_4_neighbors(grid, i, j))
	for coord in coords:
		score += dfs(grid, *coord, seen)
	return score

def part_1(grid):
	score = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '0':
				score += dfs(grid, i, j, set())
	return score

def dfs2(grid, i, j, trail_end):
	if grid[i][j] == '9':
		if (i,j) not in trail_end:
			trail_end[(i,j)] = 0
		trail_end[(i,j)] += 1
		return
	verify = lambda x: int(grid[x[0]][x[1]]) == int(grid[i][j]) + 1
	coords = filter(verify, get_bounded_4_neighbors(grid, i, j))
	for coord in coords:
		dfs2(grid, *coord, trail_end)

def part_2(grid):
	score = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '0':
				trail_end = {}
				dfs2(grid, i, j, trail_end)
				score += sum(trail_end.values())
	return score

def main(year, day):
	print(f'Day {day} - Hoof It')

	grid = get_input(year, day, type='grid', test=False)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
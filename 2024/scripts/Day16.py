from utils import *
from datetime import datetime

dirs = { 'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1) }
symbols = { 'n': '^', 'e': '>', 's': 'v', 'w': '<' }

def get_dirs(grid, x, y, path):
	new_dirs = [{'coord': (x + d[0], y + d[1]), 'dir': key} for key, d in dirs.items()]
	return list(filter(lambda d: d['coord'] not in path and grid[d['coord'][0], d['coord'][1]] != '#', new_dirs))

def dfs(grid, x, y, dir, path, min_score, score):
	if grid[x, y] == 'E':
		return score
	path.add((x, y))
	neighbors = get_dirs(grid, x, y, path)
	if not neighbors or score >= min_score:
		return float('inf')
	for n in neighbors:
		next_score = score + 1 if n['dir'] == dir else score + 1001
		if next_score >= min_score:
			continue
		min_score = min(min_score, dfs(grid, *n['coord'], n['dir'], path.copy(), min_score, score + 1 if n['dir'] == dir else score + 1001))
	return min_score

def initial_dfs(grid, x, y, dir, path, score):
	if grid[x, y] == 'E':
		return score
	path.add((x, y))
	neighbors = get_dirs(grid, x, y, path)
	if not neighbors:
		return float('inf')
	for n in neighbors:
		next_score = initial_dfs(grid, *n['coord'], n['dir'], path, score + 1 if n['dir'] == dir else score + 1001)
		if next_score != float('inf'):
			score = next_score
	return score

def part_1(grid):
	x, y = list(zip(*np.where(grid == 'S')))[0]
	initial_score = initial_dfs(grid, x, y, 'e', set(), 0)
	return dfs(grid, x, y, 'e', set(), initial_score, 0)

def part_2(grid):
	pass

def main(year, day):
	print(f'Day {day} - Reindeer Maze')

	grid = get_input(year, day, type='np_grid', test=False)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
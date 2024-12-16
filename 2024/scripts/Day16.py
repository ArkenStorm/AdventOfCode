from utils import *
from datetime import datetime
import heapq as hq

dirs = { 'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1) }
flip = { 'n': 's', 'e': 'w', 's': 'n', 'w': 'e' }

def get_dirs(grid, x, y, path):
	new_dirs = [{'coord': (x + d[0], y + d[1]), 'dir': key} for key, d in dirs.items()]
	return list(filter(lambda d: d['coord'] not in path and grid[d['coord'][0], d['coord'][1]] != '#', new_dirs))

source_map = {}

def dijkstra(grid, q, dest='E'):
	min_score = float('inf')
	for score, coord, d in q:
		source_map[(coord, d)] = 0
	path = set()
	while len(q) > 0:
		score, coord, d = hq.heappop(q)
		if source_map[(coord, d)] < score:
			continue
		if grid[coord[0], coord[1]] == dest:
			min_score = min(min_score, score)
		if (coord, d) in path:
			continue
		path.add((coord, d))
		for n in get_dirs(grid, *coord, path):
			next_coord = n['coord'] if d == n['dir'] else coord
			next_score = score + 1 if d == n['dir'] else score + 1000
			if (next_coord, n['dir']) not in source_map or next_score < source_map[(next_coord, n['dir'])]:
				source_map[(next_coord, n['dir'])] = next_score
			hq.heappush(q, (next_score, next_coord, n['dir']))
	return min_score

def part_1(grid):
	x, y = list(zip(*np.where(grid == 'S')))[0]
	queue = [(0, (x, y), 'e')]
	hq.heapify(queue)
	return dijkstra(grid, queue)

def part_2(grid, min_score):
	x, y = list(zip(*np.where(grid == 'E')))[0]
	queue = [(0, (x, y), cdir) for cdir in 'nesw']
	hq.heapify(queue)
	start_source = source_map.copy()
	source_map.clear()
	dijkstra(grid, queue)
	end_source = source_map
	best_path_tiles = set()
	# get path halves
	for i, j in np.ndindex(grid.shape):
		for dir in 'nesw':
			s, e = ((i, j), dir), ((i, j), flip[dir])
			if s in start_source and e in end_source and start_source[s] + end_source[e] == min_score:
				best_path_tiles.add((i, j))
	return len(best_path_tiles)

def main(year, day):
	print(f'Day {day} - Reindeer Maze')

	grid = get_input(year, day, type='np_grid', test=False)

	p1_start = datetime.now()
	min_score = part_1(grid)
	print(f'Part 1: {min_score}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid, min_score)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
from utils import *
from datetime import datetime
from collections import Counter

track = {}

def standard_race(grid, start, end):
	current = start
	total_time = 0

	while current != end:
		track[current] = total_time
		current = list(filter(lambda c: c not in track and grid[c[0], c[1]] != '#', apply_deltas_4(*current)))[0]
		total_time += 1
	track[current] = total_time

def cheat(grid, x, y):
	return [
		track[(x + 2*dx, y + 2*dy)] - track[(x, y)] - 2
		for dx, dy in deltas_4
		if (x + 2*dx, y + 2*dy) in track and grid[x + dx, y + dy] == '#'
	]

def cheat_2(grid, x, y):
	pass

def part_1(grid):
	cheat_times = [t for x, y in track.keys() for t in cheat(grid, x, y)]
	# times_saved = Counter(list(filter(lambda t: t > 0, cheat_times)))
	# print(sorted(times_saved.items(), key=lambda x: x[0]))
	return len(list(filter(lambda t: t >= 100, cheat_times)))

def part_2(grid):
	cheat_times = [t for x, y in track.keys() for t in cheat_2(grid, x, y)]
	times_saved = Counter(list(filter(lambda t: t > 0, cheat_times)))
	print(sorted(times_saved.items(), key=lambda x: x[0]))
	return len(list(filter(lambda t: t >= 100, cheat_times)))

def main(year, day):
	print(f'Day {day} - Race Condition')

	grid = get_input(year, day, type='np_grid', test=True)
	start = list(zip(*np.where(grid == 'S')))[0]
	end = list(zip(*np.where(grid == 'E')))[0]
	standard_race(grid, start, end)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(grid)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(grid)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
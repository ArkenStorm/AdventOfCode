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

def manhattan_coords(cheat_time):
	for dx in range(-cheat_time, cheat_time + 1):
		for dy in range(-cheat_time, cheat_time + 1):
			if dx == 0 and dy == 0: continue
			manhattan = abs(dx) + abs(dy)
			if manhattan > cheat_time: continue
			yield dx, dy, manhattan

def cheat(x, y, max_cheat_time):
	yield from (
		track[(x + dx, y + dy)] - track[(x, y)] - manhattan
		for dx, dy, manhattan in manhattan_coords(max_cheat_time)
		if (x + dx, y + dy) in track
	)

def part_1():
	cheat_times = [t for x, y in track.keys() for t in cheat(x, y, 2)]
	# times_saved = Counter(list(filter(lambda t: t >= 0, cheat_times)))
	# print(sorted(times_saved.items(), key=lambda x: x[0]))
	return len(list(filter(lambda t: t >= 100, cheat_times)))

def part_2():
	cheat_times = [t for x, y in track.keys() for t in cheat(x, y, 20)]
	# times_saved = Counter(list(filter(lambda t: t >= 50, cheat_times)))
	# print(sorted(times_saved.items(), key=lambda x: x[0]))
	return len(list(filter(lambda t: t >= 100, cheat_times)))

def main(year, day):
	print(f'Day {day} - Race Condition')

	grid = get_input(year, day, type='np_grid', test=False)
	start = list(zip(*np.where(grid == 'S')))[0]
	end = list(zip(*np.where(grid == 'E')))[0]
	standard_race(grid, start, end)

	p1_start = datetime.now()
	print(f'Part 1: {part_1()}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2()}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
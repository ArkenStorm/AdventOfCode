from utils import *
from datetime import datetime
from itertools import combinations

def part_1(schematics):
	schematics = [{(i, j) for i, row in enumerate(s.splitlines()) for j, cell in enumerate(row) if cell == '#'} for s in schematics]
	return sum(1 for s1, s2 in combinations(schematics, 2) if not set.intersection(s1, s2))

def part_2():
	return 'Merry Christmas!'

def main(year, day):
	print(f'Day {day} - Code Chronicle')

	input = get_input(year, day, type='other', test=False)
	schematics = input.split('\n\n')

	p1_start = datetime.now()
	print(f'Part 1: {part_1(schematics)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2()}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
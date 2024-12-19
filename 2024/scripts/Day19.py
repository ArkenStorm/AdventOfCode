from utils import *
from datetime import datetime
from functools import cache

patterns = []

@cache
def find_combinations(design):
	if design == '': return 1
	return sum(find_combinations(design[len(p):]) for p in patterns if design.startswith(p))


def part_1(designs):
	return sum(find_combinations(design) > 0 for design in designs)

def part_2(designs):
	return sum(find_combinations(design) for design in designs)

def main(year, day):
	global patterns
	print(f'Day {day} - Linen Layout')

	input = get_input(year, day, type='other', test=False)
	patterns, designs = input.split('\n\n')
	patterns, designs = patterns.split(', '), designs.split('\n')

	p1_start = datetime.now()
	print(f'Part 1: {part_1(designs)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(designs)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
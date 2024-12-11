from utils import *
from datetime import datetime

# (stone number, iterations left) -> resulting stones after rule application
cache = {}

def apply_rules(stone, iterations):
	if iterations == 0:
		return 1
	if (stone, iterations) in cache:
		return cache[(stone, iterations)]
	if stone == '0':
		cache[(stone, iterations)] = apply_rules('1', iterations - 1)
	elif len(stone) % 2 == 0:
		l, r = stone[:len(stone) // 2], stone[len(stone) // 2:]
		cache[(stone, iterations)] = apply_rules(str(int(l)), iterations - 1) + apply_rules(str(int(r)), iterations - 1)
	else:
		cache[(stone, iterations)] = apply_rules(str(int(stone) * 2024), iterations - 1)
	return cache[(stone, iterations)]

def part_1(stones):
	return sum(apply_rules(stone, 25) for stone in stones)

def part_2(stones):
	return sum(apply_rules(stone, 75) for stone in stones)

def main(year, day):
	print(f'Day {day} - Plutonian Pebbles')

	input = get_input(year, day, test=False)

	stones = input[0].split()

	p1_start = datetime.now()
	print(f'Part 1: {part_1(stones)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(stones)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
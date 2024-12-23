from utils import *
from datetime import datetime

is_safe = lambda arr: all(1 <= abs(x - y) <= 3 for x, y in zip(arr, arr[1:])) and (arr == sorted(arr) or arr == sorted(arr, reverse=True))

def part_1(lines):
	return sum(map(is_safe, lines))

def part_2(lines):
	dampener = lambda arr: any(is_safe(arr[:i] + arr[i + 1:]) for i in range(len(arr)))
	return sum(map(dampener, lines))

def main(year, day):
	print(f'Day {day} - Red-Nosed Reports')

	input = get_input(year, day)
	lines = [list(map(int, line.split())) for line in input]

	p1_start = datetime.now()
	print(f'Part 1: {part_1(lines)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(lines)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
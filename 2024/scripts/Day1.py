from utils import *
from datetime import datetime
import re
from collections import Counter

def part_1(left, right):
	return sum(map(lambda x: abs(x[0] - x[-1]), zip(left, right)))

def part_2(left, right):
	occurrences = Counter(right)
	return sum(map(lambda x: x * occurrences[x], left))

def main(year, day):
	print(f'Day {day} - Historian Hysteria')
	
	input = get_input(year, day)

	left, right = [], []

	for line in input:
		l, r = re.split(r'[\n\t\f\v\r ]+', line)
		left.append(l)
		right.append(r)

		left = sorted(map(int, left))
		right = sorted(map(int, right))

	p1_start = datetime.now()
	print(f'Part 1: {part_1(left, right)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(left, right)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
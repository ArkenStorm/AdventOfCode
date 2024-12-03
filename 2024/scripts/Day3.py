from utils import *
from datetime import datetime
import re

def part_1(input):
	total = 0
	for line in input:
		for match in re.findall(r'mul\((\d+),(\d+)\)', line):
			total += int(match[0]) * int(match[1])
	return total

def part_2(input):
	total = 0
	enabled = True

	for line in input:
		for match in re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', line):
			if match[0] == 'do()':
				enabled = True
			elif match[0] == 'don\'t()':
				enabled = False
			elif enabled:
				total += int(match[1]) * int(match[2])
	return total


def main(year, day):
	print(f'Day {day} - Mull It Over')
	
	input = get_input(year, day, test=False)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(input)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(input)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
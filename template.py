from utils import *
from datetime import datetime

def part_1(input):
	pass

def part_2(input):
	pass

def main(year, day):
	print(f'Day {day} - Title')

	# input = get_input(year, day)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(input)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(input)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
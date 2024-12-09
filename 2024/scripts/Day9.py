from utils import *
from datetime import datetime

def part_1(input):
	ids = { id: (id, int(size)) for id, size in enumerate(input[::2]) }
	print(ids)
	free_spaces = input[1::2]


	system_map = ''
	for id, size in enumerate(input):
		if id % 2 == 0:
			system_map += str(str(id // 2) * int(size))
		else:
			system_map += str('.' * int(size))

	start, end = 0, len(system_map) - 1
	while system_map[end] == '.': end -= 1

	system_map = list(system_map)

	while start < end:
		if system_map[start] == '.':
			system_map[start], system_map[end] = system_map[end], system_map[start]
			while system_map[end] == '.': end -= 1
		start += 1

	system_map = list(filter(lambda x: x != '.', system_map))
	system_map = ''.join(system_map)
	return sum(int(val) * i for i, val in enumerate(system_map))

def part_2(input):
	pass

def main(year, day):
	print(f'Day {day} - Disk Fragmenter')

	input = get_input(year, day, test=True)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(input[0])}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(input)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
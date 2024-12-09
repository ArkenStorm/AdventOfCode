from utils import *
from datetime import datetime

def part_1(system_map):
	start, end = 0, len(system_map) - 1
	while system_map[end] == '.': end -= 1

	while start < end:
		if system_map[start] == '.':
			system_map[start], system_map[end] = system_map[end], system_map[start]
			while system_map[end] == '.': end -= 1
		start += 1

	filtered_system_map = list(filter(lambda x: x != '.', system_map))
	return sum(int(val) * i for i, val in enumerate(filtered_system_map))

def part_2(system_map, id_to_size):
	start, end = 0, len(system_map) - 1
	while system_map[end] == '.': end -= 1

	# start at the end, find the first block of free space that fits it, starting at the beginning every time.

	defragged = []
	while start < end:
		end_size = id_to_size[system_map[end]]
		free_block = start + end_size
		if system_map[start:free_block] == ['.'] * end_size:
			defragged += system_map[end - end_size + 1:end + 1]
			start += end_size
			end -= end_size
			while system_map[end] == '.': end -= 1
		elif system_map[start] == '.':
			while system_map[start] == '.':
				defragged += system_map[start]
				start += 1
		else:
			block_end = start + id_to_size[system_map[start]]
			defragged += system_map[start:block_end]
			start += id_to_size[system_map[start]]

	return sum(int(val) * i for i, val in enumerate(defragged) if val != '.')

def main(year, day):
	print(f'Day {day} - Disk Fragmenter')

	input = get_input(year, day, test=True)

	id_to_size = { str(id): int(size) for id, size in enumerate(input[0][::2]) }
	# print(id_to_size)
	# free_spaces = input[1::2]


	system_map = []
	for id, size in enumerate(input[0]):
		if id % 2 == 0:
			system_map += [str(id // 2)] * int(size)
		else:
			system_map += ['.'] * int(size)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(system_map.copy())}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(system_map.copy(), id_to_size)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
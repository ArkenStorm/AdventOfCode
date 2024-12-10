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
	og_file_pos = file_pos = len(system_map) - 1
	for id in list(id_to_size.keys())[::-1]:
		disk_pos = 0
		end_size = id_to_size[id]

		file_pos = og_file_pos
		while system_map[file_pos] != id: file_pos -= 1
		og_file_pos = file_pos - (end_size - 1)

		free_block = disk_pos + end_size
		while system_map[disk_pos:free_block] != ['.'] * end_size and disk_pos < og_file_pos:
			disk_pos += 1
			free_block = disk_pos + end_size
		if disk_pos < og_file_pos:
			for _ in range(end_size):
				system_map[disk_pos], system_map[file_pos] = system_map[file_pos], system_map[disk_pos]
				disk_pos += 1
				file_pos -= 1

	return sum(int(val) * i for i, val in enumerate(system_map) if val != '.')

def main(year, day):
	print(f'Day {day} - Disk Fragmenter')

	input = get_input(year, day, test=False)

	id_to_size = { str(id): int(size) for id, size in enumerate(input[0][::2]) }

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
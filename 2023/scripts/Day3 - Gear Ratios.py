import re
from itertools import chain

inFile = open('../inputs/Day3.txt', 'r')
schematic = inFile.read().splitlines()

print('Day 3 - Gear Ratios')

# Part 1
symbols = { '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '/' }

part_num_sum = 0
part_nums = [[] for x in range(len(schematic[0]))] # ((str)match_val, (start_idx, end_idx))

def symbol_adjacent(i, j):
	rows, cols = len(schematic), len(schematic[0])

	neighbors = [
		schematic[x][y]
		for x in range(max(0, i - 1), min(rows, i+ 2))
		for y in range(max(0, j - 1), min(cols, j + 2))
		if (x,y) != (i, j) and 0 <= x < rows and 0 <= y < cols
	]
	return any(n in symbols for n in neighbors)

for i in range(len(schematic)):
	matches = re.finditer(r"\d+", schematic[i])
	for match in matches:
		# check for symbols at every index
		start, end = match.span()
		for j in range(start, end):
			if symbol_adjacent(i, j):
				part_num_sum += int(match.group(0))
				part_nums[i].append((match.group(0), (start, end)))
				break

print(f"Part 1: {part_num_sum}")

# Part 2
gear_ratio_sum = 0

def get_adjacent_parts(i, j):
	rows, cols = len(schematic), len(schematic[0])

	adjacent_parts = [
		list(filter(lambda p: y in range(p[1][0], p[1][1]), part_nums[x]))
		for x in range(max(0, i - 1), min(rows, i+ 2))
		for y in range(max(0, j - 1), min(cols, j + 2))
		if (x,y) != (i, j) and 0 <= x < rows and 0 <= y < cols
	]

	adjacent_parts = list(set(list(chain.from_iterable(adjacent_parts))))

	return adjacent_parts


for i in range(len(schematic)):
	matches = re.finditer(r"\*", schematic[i])
	for match in matches:
		parts = get_adjacent_parts(i, match.start())
		if len(parts) == 2:
			gear_ratio_sum += int(parts[0][0]) * int(parts[1][0])

print(f"Part 2: {gear_ratio_sum}")

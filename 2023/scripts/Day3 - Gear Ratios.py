import re

inFile = open('../inputs/Day3.txt', 'r')
schematic = inFile.read().splitlines()

print('Day 3 - Gear Ratios')

# Part 1
symbols = { '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '/' }

part_num_sum = 0
part_nums = [] # ((str)match_val, (row, start_index))

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
				part_nums.append((match.group(0), (i, start)))
				break

print(f"Part 1: {part_num_sum}")

# Part 2

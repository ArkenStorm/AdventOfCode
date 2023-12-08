import numpy as np
import math

inFile = open('../inputs/Day8.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day8.txt')
lines = inFile.read().splitlines()

print('Day 8 - Haunted Wasteland')

# Part 1
directions = lines[0]
mappings = lines[2:]
direction_map = {}

for mapping in mappings:
	key, dirs = mapping.split('=')
	key, dirs = key.strip(), dirs.strip()
	dirs = dirs[1:-1].split(', ')
	direction_map[key] = dirs

curr = 'AAA'
num_steps = 0
while curr != 'ZZZ':
	for turn in directions:
		curr = direction_map[curr][0] if turn == 'L' else direction_map[curr][1]
		num_steps += 1
		if curr == 'ZZZ':
			break

print(f"Part 1: {num_steps}")


# Part 2
starts = ['AAA', 'BFA', 'VGA', 'DXA', 'VJA', 'BPA']
# starts = ['11A', '22A']
step_counts = []
for start in starts:
	curr = start
	curr_steps = 0
	while curr[2] != 'Z':
		for turn in directions:
			curr = direction_map[curr][0] if turn == 'L' else direction_map[curr][1]
			curr_steps += 1
			if curr[2] == 'Z':
				break
	step_counts.append(curr_steps)
	
print(f"Part 2: {math.lcm(*step_counts)}")
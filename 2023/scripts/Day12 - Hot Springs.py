import re
import numpy as np
from functools import reduce
from math import comb

inFile = open('../inputs/Day12.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day12.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 12 - Hot Springs')

# Part 1
solved = {}

# sp_idx: current index in spring string
# bg_idx: broken group index, i.e. index 0 for [1, 1, 3]
# curr_len: length of current broken spring block
def solver(springs, broken_groups, sp_idx, bg_idx, curr_len):
	key = (sp_idx, bg_idx, curr_len)
	if key in solved:
		return solved[key]
	if sp_idx == len(springs):  # If we're at the end of the spring string, and...
		# ...If we're either at the last broken group or we're at the penultimate broken group and our current broken spring group matches the length of the current broken group, there's only one arrangement
		if (bg_idx == len(broken_groups) and curr_len == 0) or (bg_idx == len(broken_groups) - 1 and broken_groups[bg_idx] == curr_len):
			return 1
		else:
			return 0
	arrs = 0
	for s in ['.', '#']:
		if springs[sp_idx] in f'{s}?':
			# If it's a definitely broken spring, just move onto the next spring index while increasing the length of our current group
			if s == '#':
				arrs += solver(springs, broken_groups, sp_idx + 1, bg_idx, curr_len + 1)
			# our current spring matches the spring string and we haven't started a group, move to the next spring
			elif curr_len == 0:
				arrs += solver(springs, broken_groups, sp_idx + 1, bg_idx, 0)
			# if we're in a broken spring group and not at the last broken group, and our current group length matches a valid broken group, start the group over starting at the next spring
			elif curr_len > 0 and bg_idx < len(broken_groups) and broken_groups[bg_idx] == curr_len:
				arrs += solver(springs, broken_groups, sp_idx + 1, bg_idx + 1, 0)
	solved[key] = arrs
	return arrs

for part in [1, 2]:
	total = 0
	for line in lines:
		springs, broken_groups = line.split(' ')
		if part == 2:
			springs = '?'.join([springs] * 5)
			broken_groups = ','.join([broken_groups] * 5)
		broken_groups = list(map(int, re.findall(r"\d+", broken_groups)))
		solved.clear()
		total += solver(springs, broken_groups, 0, 0, 0)
	print(f"Part {part}: {total}")
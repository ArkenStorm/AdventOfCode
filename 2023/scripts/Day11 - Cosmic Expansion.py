import numpy as np
from functools import reduce

# from aoc_utils import *

# test = False
# lines = get_input('2023', 11, test)

inFile = open('../inputs/Day11.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day11.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

cosmos = np.array([list(line) for line in lines])

print('Day 11 - Cosmic Expansion')

# Part 1
galaxies = np.argwhere(cosmos == '#')
g_rows, g_cols = set(), set()
for g in galaxies:
	g_rows.add(g[0])
	g_cols.add(g[1])

def reductor(acc, v, g_ex, dist):
	return acc + 1 if v in g_ex else acc + dist

p = 1
for expansion in [2, 1000000]: # Part 2
	total = 0
	for i in range(len(galaxies)):
		for j in range(i + 1, len(galaxies)):
			steps = 0
			x_start, x_end = sorted([galaxies[i][0], galaxies[j][0]])
			y_start, y_end = sorted([galaxies[i][1], galaxies[j][1]])
			steps += reduce(lambda acc, x: reductor(acc, x, g_rows, expansion), range(x_start, x_end), 0)
			steps += reduce(lambda acc, y: reductor(acc, y, g_cols, expansion), range(y_start, y_end), 0)
			total += steps
	print(f"Part {p}: {total}")
	p += 1
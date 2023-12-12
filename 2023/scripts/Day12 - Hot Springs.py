import re
import numpy as np
from functools import reduce
from math import comb

# inFile = open('../inputs/Day12.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day12.txt')
inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 12 - Hot Springs')

# Part 1
total = 0
for line in lines:
	springs, groups = line.split(' ')
	groups = list(map(int, re.findall(r"\d+", groups)))
	arrs = 0

	spring_groups = list(filter(lambda sp: sp != '', springs.split('.')))
	print(spring_groups)
	print(groups)

	if len(groups) == len(spring_groups):
		print(comb(2, 1))
		arrs += reduce(lambda acc, i: acc + comb(len(spring_groups[i]), groups[i]), range(len(groups)), 0)
	else:
		pass

	for sp_g in spring_groups:
		if all(c == '#' for c in sp_g): continue
		else:
			pass
	
	for g in groups:
		pass

	# for sp_g in spring_groups:
	# 	if all(c == '#' for c in sp_g):
	# 		idx = next(i for i, v in enumerate(groups) if v == len(sp_g))
	# 		groups.pop(idx)
		

	total += arrs
	# print(arrs)
print(total)
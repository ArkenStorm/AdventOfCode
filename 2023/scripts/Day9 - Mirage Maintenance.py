import numpy as np

inFile = open('../inputs/Day9.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day9.txt')
lines = inFile.read().splitlines()

print('Day 9 - Mirage Maintenance')

part1, part2 = 0, 0

for line in lines:
	seq = list(map(int, line.split()))
	curr_diff = np.diff(seq)
	diffs = [seq, np.diff(seq)]
	while not all(d == 0 for d in curr_diff):
		curr_diff = np.diff(curr_diff)
		diffs.append(curr_diff)
	
	p1_prev, p2_prev = 0, 0
	for i in range(len(diffs) - 2, -1, -1):
		p1_prev += diffs[i][-1]
		p2_prev = diffs[i][0] - p2_prev
	part1 += p1_prev
	part2 += p2_prev

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
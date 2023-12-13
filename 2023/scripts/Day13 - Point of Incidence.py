import numpy as np
from functools import reduce

inFile = open('../inputs/Day13.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day13.txt')
# inFile = open('2023/inputs/test.txt', 'r')
patterns = inFile.read().split('\n\n')

print('Day 13 - Point of Incidence')

patterns = [np.array([list(line) for line in pattern.split('\n')]) for pattern in patterns]

reflections = {}  # pattern_idx: (index, vertical=True) # horizontal False

def check_reflection(pattern, vertical):
	sequence = pattern[0] if vertical else pattern
	for i in range(len(sequence) - 1):
		if vertical:
			first, second = sequence[i], sequence[i+1]
		else:
			first, second = sequence[i][0], sequence[i+1][0]
		if first == second:
			b, f = i, i + 1
			is_mirrored = True
			while b >= 0 and f < len(sequence) and is_mirrored:
				if vertical:
					b_slice, f_slice = pattern[:,b:b+1], pattern[:,f:f+1]
				else:
					b_slice, f_slice = pattern[b:b+1,:], pattern[f:f+1,:]
				if not np.array_equal(b_slice, f_slice):
					is_mirrored = False
					break
				b -= 1
				f += 1
			if is_mirrored:
				return i + 1
	return 0

total_cols, total_rows = 0, 0
for pattern in patterns:
	total_cols += check_reflection(pattern, True)
	total_rows += check_reflection(pattern, False)

total = total_cols + (total_rows * 100)
print(f"Part 1: {total}")
import numpy as np
from functools import reduce
from itertools import chain

# inFile = open('../inputs/Day13.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day13.txt')
inFile = open('2023/inputs/test.txt', 'r')
patterns = inFile.read().split('\n\n')

print('Day 13 - Point of Incidence')

patterns = [np.array([list(line) for line in pattern.split('\n')]) for pattern in patterns]

reflections = {}  # pattern: (index, vertical=True) # horizontal False

# Part 1
def check_reflection(pattern, pattern_idx, vertical: bool, smudges=0):
	sequence = pattern[0] if vertical else pattern
	for i in range(len(sequence) - 1):
		if vertical:
			first, second = sequence[i], sequence[i+1]
		else:
			first, second = sequence[i][0], sequence[i+1][0]
		if first == second:
			b, f = i, i + 1
			is_mirrored = True
			diffs = 0
			while b >= 0 and f < len(sequence) and is_mirrored and diffs <= smudges:
				if vertical:
					b_slice, f_slice = pattern[:,b:b+1], pattern[:,f:f+1]
				else:
					b_slice, f_slice = pattern[b:b+1,:], pattern[f:f+1,:]
				if not np.array_equal(b_slice, f_slice):
					if smudges:
						flat_b_slice, flat_f_slice = list(chain.from_iterable(b_slice)), list(chain.from_iterable(f_slice))
						for i in range(len(flat_b_slice)):
							if flat_b_slice[i] != flat_f_slice[i]:
								diffs += 1
							if diffs > smudges:
								is_mirrored = False
								break
					else:
						is_mirrored = False
						break
				b -= 1
				f += 1
			if is_mirrored:
				val = (i, vertical)
				if pattern_idx not in reflections or reflections[pattern_idx] != val:
					reflections[pattern_idx] = (i, vertical)
					return i + 1
				else:
					continue
	return 0

total_cols, total_rows = 0, 0
for idx, pattern in enumerate(patterns):
	total_cols += check_reflection(pattern, idx, True)
	total_rows += check_reflection(pattern, idx, False)

total = total_cols + (total_rows * 100)
print(f"Part 1: {total}")

# Part 2
total_cols, total_rows = 0, 0
for idx, pattern in enumerate(patterns):
	total_cols += check_reflection(pattern, idx, True, 1)
	total_rows += check_reflection(pattern, idx, False, 1)

total = total_cols + (total_rows * 100)
print(f"Part 2: {total}")
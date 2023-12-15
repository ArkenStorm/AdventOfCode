from functools import reduce

inFile = open('../inputs/Day15.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day15.txt')
# inFile = open('2023/inputs/test.txt', 'r')
sequence = inFile.read().split(',')

print('Day 15 - Lens Library')

# Part 1
def hash(seq):
	return reduce(lambda acc, c: 17*(acc + ord(c)) % 256, seq, 0)

hashed = sum(hash(s) for s in sequence)

print(f"Part 1: {hashed}")

# Part 2
boxes = [dict() for _ in range(256)]

for op in sequence:
	if '=' in op:
		lens, focus = op.split('=')
		boxes[hash(lens)][lens] = int(focus)
	else:
		lens, _ = op.split('-')
		boxes[hash(lens)].pop(lens, None)

focus_power = reduce(lambda acc, box: acc + sum(slot * focus for slot, (_, focus) in enumerate(box[1].items(), 1)) * box[0], enumerate(boxes, 1), 0)

print(f"Part 2: {focus_power}")
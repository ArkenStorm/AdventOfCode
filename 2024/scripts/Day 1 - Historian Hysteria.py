import re
from collections import Counter

# inFile = open('../inputs/Day1.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2024/inputs/Day1.txt', 'r')
# inFile = open('2024/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 1 - Historian Hysteria')

# Part 1
left, right = [], []

for line in lines:
	l, r = re.split(r'[\n\t\f\v\r ]+', line)
	left.append(l)
	right.append(r)

left = sorted(map(int, left))
right = sorted(map(int, right))

p1_total = sum(map(lambda x: abs(x[0] - x[-1]), zip(left, right)))
print(f'Part 1: {p1_total}')

# Part 2
occurrences = Counter(right)
p2_total = sum(map(lambda x: x * occurrences[x], left))

print(f'Part 2: {p2_total}')
from utils import *
from datetime import datetime
from functools import cache
from collections import defaultdict

@cache
def mix_prune(n, m):
	return (n ^ m) % 16777216

@cache
def next_secret_num(n):
	n = mix_prune(n, n * 64)
	n = mix_prune(n, n // 32)
	n = mix_prune(n, n * 2048)
	return n

def part_1(secret_nums):
	total = 0
	for n in secret_nums:
		for _ in range(2000):
			n = next_secret_num(n)
		total += n
	return total

def part_2(secret_nums):
	banana_haul = defaultdict(int)
	for n in secret_nums:
		unit = n % 10 # last digit
		changes = [] # tuple of (change, value)
		for _ in range(2000):
			n = next_secret_num(n)
			next_unit = n % 10
			changes.append((next_unit - unit, next_unit))
			unit = next_unit
		patterns = set()
		# check every 4 consecutive changes
		for i in range(len(changes) - 3):
			p = tuple(c[0] for c in changes[i:i + 4])
			if p not in patterns:
				patterns.add(p)
				banana_haul[p] += changes[i + 3][1] # get value of last change in sequence
	return max(banana_haul.values())

def main(year, day):
	print(f'Day {day} - Monkey Market')

	secret_nums = [int(x) for x in get_input(year, day, test=False)]

	p1_start = datetime.now()
	print(f'Part 1: {part_1(secret_nums)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(secret_nums)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
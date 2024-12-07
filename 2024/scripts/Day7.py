from utils import *
from datetime import datetime
from math import log10
from functools import reduce
from operator import add, mul

def concat_ints(x, y): # stolen from reddit for optimization
    return x * (10 ** (int(log10(y)) + 1)) + y  # int(str(x) + str(y))

def is_valid_eq(target, operands, operators):
	reductor = lambda acc, n: [res for partial in acc for op in operators if (res := op(partial, n)) <= target]
	results = reduce(reductor, operands[1:], [operands[0]])
	return target in results

def get_total(input, operators):
	return sum(target for target, operands in input if is_valid_eq(target, operands, operators))

def part_1(input):
	return get_total(input, [add, mul])

def part_2(input):
	return get_total(input, [add, mul, concat_ints])

def main(year, day):
	print(f'Day {day} - Bridge Repair')

	input = get_input(year, day, test=False)

	# format input better
	input = [(int(target), list(map(int, operands.split()))) for target, operands in (eq.split(':') for eq in input)]

	p1_start = datetime.now()
	print(f'Part 1: {part_1(input)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(input)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
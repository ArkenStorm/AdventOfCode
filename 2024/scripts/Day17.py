from utils import *
from datetime import datetime
import re

registers = { 'a': 0, 'b': 0, 'c': 0 }
combo_ops = {
	0: 0,
	1: 1,
	2: 2,
	3: 3,
	4: lambda: registers['a'],
	5: lambda: registers['b'],
	6: lambda: registers['c'],
	7: lambda: print('Reserved, program invalid')
}

def get_combo_op(operand):
	return combo_ops[operand] if type(combo_ops[operand]) == int else combo_ops[operand]()

def adv(operand):
	registers['a'] //= 2**get_combo_op(operand)

def bxl(operand):
	registers['b'] ^= operand

def bst(operand):
	registers['b'] = get_combo_op(operand) % 8

# set iptr to return value of jnz if not none
def jnz(operand):
	return operand if registers['a'] != 0 else None

def bxc(_):
	registers['b'] = registers['b'] ^ registers['c']

def out(operand, output: list):
	output.append(get_combo_op(operand) % 8)

def bdv(operand):
	registers['b'] = registers['a'] // 2**get_combo_op(operand)

def cdv(operand):
	registers['c'] = registers['a'] // 2**get_combo_op(operand)

def part_1(program):
	iptr = 0
	output = []
	while iptr < len(program):
		op, operand = program[iptr], program[iptr + 1]
		ret = None
		if op == 0: adv(operand)
		elif op == 1: bxl(operand)
		elif op == 2: bst(operand)
		elif op == 3: ret = jnz(operand)
		elif op == 4: bxc(operand)
		elif op == 5: out(operand, output)
		elif op == 6: bdv(operand)
		elif op == 7: cdv(operand)
		iptr = ret if ret is not None else iptr + 2
	return ','.join(map(str, output))

def part_2(program):
	# track all operations and values at each step from part 1?
	pass

def main(year, day):
	print(f'Day {day} - Chronospatial Computer')

	input = get_input(year, day, type='other', test=False)
	rs, p = input.split('\n\n')
	registers['a'] = int(re.findall(r'\d+', rs)[0])
	program = list(map(int, p[9:].split(',')))

	p1_start = datetime.now()
	print(f'Part 1: {part_1(program)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(program)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
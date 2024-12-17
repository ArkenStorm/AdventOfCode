from utils import *
from datetime import datetime
import re

registers = { 'a': 0, 'b': 0, 'c': 0 }
combo_ops = { 0: 0, 1: 1, 2: 2, 3: 3, 4: lambda: registers['a'], 5: lambda: registers['b'], 6: lambda: registers['c'], 7: lambda: print('Reserved, program invalid') }

def get_combo_op(operand):
	return combo_ops[operand] if type(combo_ops[operand]) == int else combo_ops[operand]()

def run_program(program):
	iptr = 0
	output = []
	while iptr < len(program):
		op, operand = program[iptr], program[iptr + 1]
		ret = None
		if op == 0: registers['a'] //= 2**get_combo_op(operand) # adv
		elif op == 1: registers['b'] ^= operand # bxl
		elif op == 2: registers['b'] = get_combo_op(operand) % 8 # bst
		elif op == 3: ret = operand if registers['a'] != 0 else None # jnz
		elif op == 4: registers['b'] = registers['b'] ^ registers['c'] # bxc
		elif op == 5: output.append(get_combo_op(operand) % 8) # out
		elif op == 6: registers['b'] = registers['a'] // 2**get_combo_op(operand) # bdv
		elif op == 7: registers['c'] = registers['a'] // 2**get_combo_op(operand) # cdv
		iptr = ret if ret is not None else iptr + 2
	return output

def part_1(program):
	return ','.join(map(str, run_program(program)))

def part_2(program):
	q = [(len(program) - 1, 0)] # program always ends with zero
	while len(q) > 0:
		i, opcode = q.pop(0)
		for op in range(8):
			reg_val = (opcode << 3) + op
			registers['a'] = reg_val
			if run_program(program) == program[i:]:
				if i == 0: return reg_val
				q.append((i - 1, reg_val))
	return None

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
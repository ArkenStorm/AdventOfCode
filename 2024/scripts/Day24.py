from utils import *
from datetime import datetime
from collections import defaultdict
from operator import and_, or_, xor
import re

wires, sources = defaultdict(int), defaultdict(dict)
ops = {'AND': and_, 'OR': or_, 'XOR': xor}

def get_bin_str(c):
	c_wires = sorted([w for w in wires.keys() if w.startswith(c)], reverse=True, key=lambda x: int(x[1:]))
	return ''.join([str(wires[w]) for w in c_wires])

def update_wires():
	has_changed = True
	while has_changed:
		has_changed = False
		for d in sources:
			w1, op, w2 = sources[d]
			prev = wires[d]
			wires[d] = ops[op](wires[w1], wires[w2])
			if prev != wires[d]:
				has_changed = True

def part_1(gates):
	global sources
	sources = {dst: (w1, op, w2) for w1, op, w2, dst in re.findall(r'(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})', gates)}
	update_wires()
	return int(get_bin_str('z'), 2)

# doesn't work for test input
def part_2():
	highest_z = max([w for w in wires.keys() if w.startswith('z')], key=lambda x: int(x[1:]))
	wrong = set()
	for out_wire, (w1, op, w2) in sources.items():
		if (
			(out_wire.startswith('z') and op != 'XOR' and out_wire != highest_z) or
			(op == 'XOR' and all(w[0] not in 'xyz' for w in (out_wire, w1, w2)))
		):
			wrong.add(out_wire)
			continue

		for sub_w1, sub_op, sub_w2 in sources.values():
			if (op == 'AND' and 'x00' not in (w1, w2) and (out_wire == sub_w1 or out_wire == sub_w2) and sub_op != 'OR'):
				wrong.add(out_wire)
				break
			if (op == 'XOR' and (out_wire == sub_w1 or out_wire == sub_w2) and sub_op == 'OR'):
				wrong.add(out_wire)
				break
	return ','.join(sorted(list(wrong)))

def main(year, day):
	print(f'Day {day} - Crossed Wires')

	input = get_input(year, day, type='other', test=False)
	starting, gates = input.split('\n\n')
	for s in starting.split('\n'):
		w, v = s.split(': ')
		wires[w] = int(v)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(gates)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2()}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
from utils import *
from datetime import datetime
from functools import cache
from itertools import permutations

numpad = { b: (x // 3, x % 3) for x, b in enumerate('789456123_0A') if b != '_' }
dirpad = { b: (x // 3, x % 3) for x, b in enumerate('_^A<v>') if b != '_' }
dirs = { '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1) }

@cache
def get_presses(moves, robots=2, use_nums=True, start=None):
	pad = numpad if use_nums else dirpad
	if not moves: return 0
	if not start: start = pad['A']

	(sx, sy), (tx, ty) = start, pad[moves[0]]
	dx, dy = tx - sx, ty - sy

	buttons = ''
	if dx < 0: buttons += '^' * -dx
	elif dx > 0: buttons += 'v' * dx
	if dy < 0: buttons += '<' * -dy
	elif dy > 0: buttons += '>' * dy

	if robots:
		permutation_lens = []
		for p in set(permutations(buttons)):
			x, y = start
			for m in p:
				dx, dy = dirs[m]
				x, y = x + dx, y + dy
				if (x, y) not in pad.values(): break
			else:
				permutation_lens.append(get_presses(p + ('A',), robots - 1, False))
		min_len = min(permutation_lens)
	else:
		min_len = len(buttons) + 1 # add 'A' press
	return min_len + get_presses(moves[1:], robots, use_nums, (tx, ty))

def part_1(codes):
	return sum(int(code[:-1]) * get_presses(code, 2) for code in codes)

def part_2(codes):
	return sum(int(code[:-1]) * get_presses(code, 25) for code in codes)

def main(year, day):
	print(f'Day {day} - Keypad Conundrum')

	codes = get_input(year, day, test=False)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(codes)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(codes)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
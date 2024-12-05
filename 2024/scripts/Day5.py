from utils import *
from datetime import datetime
from collections import defaultdict

invalid_updates = []

def part_1(dependencies, updates):
	valid_updates = []

	for update in updates:
		order = update.split(',')
		update_is_good = True
		for i in range(len(order) - 1, -1, -1):
			if any(order[i] in dependencies[x] for x in order[:i]):
				update_is_good = False
				invalid_updates.append(update)
				break
		if update_is_good:
			valid_updates.append(update)

	# works but is slower
	# for update in updates:
	# 	order = update.split(',')
	# 	if all(not any(order[i] in dependencies[x] for x in order[:i]) for i in range(len(order))):
	# 		valid_updates.append(update)
	# 	else:
	# 		invalid_updates.append(update)

	return sum(int(u.split(',')[len(u.split(',')) // 2]) for u in valid_updates)

def part_2(dependencies):
	fixed_updates = []
	for update in invalid_updates:
		order = update.split(',')
		i = 0
		while i < len(order) - 1:
			if order[i + 1] in dependencies[order[i]]:
				order[i], order[i + 1] = order[i + 1], order[i]
				i = max(i - 1, 0)
			else:
				i += 1
		fixed_updates.append(order)

	return sum(int(u[len(u) // 2]) for u in fixed_updates)

def main(year, day):
	print(f'Day {day} - Print Queue')

	input = get_input(year, day, type='other', test=False)

	order_rules, updates = input.split('\n\n')
	order_rules = order_rules.split('\n')
	updates = updates.split('\n')

	dependencies = defaultdict(set)

	for rule in order_rules:
		dep, key = rule.split('|')
		dependencies[key].add(dep)

	p1_start = datetime.now()
	print(f'Part 1: {part_1(dependencies, updates)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(dependencies)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
import re
from functools import reduce

inFile = open('../inputs/Day19.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day19.txt')
# inFile = open('2023/inputs/test.txt', 'r')
rules, parts = inFile.read().split('\n\n')
rules, parts = rules.split('\n'), parts.split('\n')

ops = { '<': lambda a, b: a < b, '>': lambda a, b: a > b }

print('Day 19 - Aplenty')

rule_re = r"(\w+){(.*)}"
cond_re = r"([xmas])([<>])(\d+):(\w+)"

# workflows
wfs = {}

for rule in rules:
	workflow, conditions = re.match(rule_re, rule).groups()
	conditions = conditions.split(',')
	parsed_conditions = []
	for cond in conditions:
		if ':' in cond:
			prop, op, val, dest = re.match(cond_re, cond).groups()
			parsed_conditions.append((prop, op, int(val), dest))
		else:
			parsed_conditions.append((cond,))
	wfs[workflow] = parsed_conditions


# Part 1
accepted = []

def send_to_dest(part, dest):
	if dest == 'A':
		accepted.append(part)
		return
	elif dest == 'R':
		return
	else:
		return process_part(part, dest)

def process_part(part, wf):
	conditions = wfs[wf]
	for cond in conditions:
		if len(cond) == 1:
			return send_to_dest(part, cond[0])
		else:
			prop, op, val, dest = cond
			if ops[op](part[prop], val):
				return send_to_dest(part, dest)

part_re = r"([xmas])=(\d+)"

for part in parts:
	parsed_part = {}
	for prop, val in re.findall(part_re, part):
		parsed_part[prop] = int(val)

	process_part(parsed_part, 'in')

accepted_ratings = reduce(lambda acc, p: acc + sum(p.values()), accepted, 0)
print(f"Part 1: {accepted_ratings}")

# Part 2
ranges = { 'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000] }
combos = 0

def handle_dest(dest, r: dict):
	global combos

	if dest == 'A':
		combos += reduce(lambda acc, p: acc * (abs(r[p][1] - r[p][0]) + 1), r, 1)
		return
	elif dest == 'R':
		return
	else:
		return find_ranges(dest, r)

# r is the current working range
def find_ranges(wf, r: dict):
	conditions = wfs[wf]
	for cond in conditions:
		if len(cond) == 1:
			return handle_dest(cond[0], r)
		else:
			# split range at val
			prop, op, val, dest = cond
			pass_copy = r.copy()
			if op == '<':
				pass_copy[prop] = [r[prop][0], val - 1]
				r[prop] = [val, r[prop][1]]
			else:
				pass_copy[prop] = [val + 1, r[prop][1]]
				r[prop] = [r[prop][0], val]
			handle_dest(dest, pass_copy)
			# continue with current r

find_ranges('in', ranges)


print(f"Part 2: {combos}")
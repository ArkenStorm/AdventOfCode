import re
from functools import reduce
# import operator
# import sys
# sys.setrecursionlimit(10000)

# inFile = open('../inputs/Day19.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day19.txt')
inFile = open('2023/inputs/test.txt', 'r')
rules, parts = inFile.read().split('\n\n')
rules, parts = rules.split('\n'), parts.split('\n')

# ops = { '<': operator.lt, '>': operator.gt }
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
accepted, acc_set = [], set()

def send_to_dest(part, dest):
	part_str = str(part)
	if dest == 'A':
		if part_str not in acc_set:
			accepted.append(part)
			acc_set.add(part_str)
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
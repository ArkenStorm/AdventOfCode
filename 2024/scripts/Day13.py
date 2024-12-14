from utils import *
from datetime import datetime
import re
# from pulp import LpProblem, LpVariable, LpMinimize, PULP_CBC_CMD
# from z3 import Int, Optimize, sat

# part 1 works, part 2 doesn't??? PuLP why have you failed me
# def solve(machines, p2=False):
# 	lowBound = 100 if p2 else 0
# 	upBound = None if p2 else 100
# 	tokens = 0
# 	for machine in machines:
# 		problem = LpProblem('Minimize_Button_Cost', LpMinimize)
# 		a = LpVariable('a', lowBound, upBound, cat='Integer')
# 		b = LpVariable('b', lowBound, upBound, cat='Integer')
# 		cost = 3 * a + 1 * b
# 		problem += machine['a'][0] * a + machine['b'][0] * b == machine['p'][0], 'X_Target'
# 		problem += machine['a'][1] * a + machine['b'][1] * b == machine['p'][1], 'Y_Target'
# 		problem += cost
# 		status = problem.solve(PULP_CBC_CMD(msg=0))
# 		if status == 1:
# 			# print(f'A Presses: {int(a.varValue)}, B Presses: {int(b.varValue)}, Cost: {int(cost.value())}')
# 			tokens += int(cost.value())
# 	return tokens

# def part_2(machines):
# 	for machine in machines:
# 		machine['p'] = (machine['p'][0] + 10000000000000, machine['p'][1] + 10000000000000)

# 	return solve(machines, True)

# Z3 time baby
# def solve(machines):
# 	tokens = 0
# 	for machine in machines:
# 		opt = Optimize()
# 		a, b = Int('a'), Int('b')
# 		opt.add(machine['a'][0] * a + machine['b'][0] * b == machine['p'][0])
# 		opt.add(machine['a'][1] * a + machine['b'][1] * b == machine['p'][1])
# 		opt.minimize(3 * a + b)
# 		if opt.check() == sat:
# 			model = opt.model()
# 			tokens += 3 * model[a].as_long() + model[b].as_long()
# 	return tokens


# Cramer's Rule of Linear Algebra; This is the optimal solution, also the fastest
def det(a, b):
	return a[0] * b[1] - a[1] * b[0]

def get_vector(a, b, p):
	D, Dx, Dy = det(a, b), det(p, b), det(a, p)
	return (Dx // D, Dy // D) if Dx % D == 0 and Dy % D == 0 else (0, 0)

def cost(vector):
	return 3 * vector[0] + vector[1]

def solve(machines):
	return sum(cost(get_vector(*m)) for m in machines)

def part_1(machines):
	return solve(machines)

def part_2(machines):
	for m in machines:
		m['p'] = (m['p'][0] + 10000000000000, m['p'][1] + 10000000000000)

	return solve(machines)

def main(year, day):
	print(f'Day {day} - Claw Contraption')

	input = get_input(year, day, type='other', test=False)

	groups = input.split('\n\n')
	machines = []

	for group in groups:
		machine = group.splitlines()
		reg = r'\d+'
		ax, ay = re.findall(reg, machine[0])
		bx, by = re.findall(reg, machine[1])
		px, py = re.findall(reg, machine[2])
		machines.append({ 'a': (int(ax), int(ay)), 'b': (int(bx), int(by)), 'p': (int(px), int(py)) })

	p1_start = datetime.now()
	print(f'Part 1: {part_1(machines)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(machines)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
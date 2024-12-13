from utils import *
from datetime import datetime
import re
from pulp import LpProblem, LpVariable, LpMinimize, PULP_CBC_CMD

def part_1(machines):
	tokens = 0
	for machine in machines:
		problem = LpProblem('Minimize_Button_Cost', LpMinimize)
		a = LpVariable('a', lowBound=0, upBound=100, cat='Integer')
		b = LpVariable('b', lowBound=0, upBound=100, cat='Integer')
		cost = 3 * a + 1 * b
		problem += machine['a'][0] * a + machine['b'][0] * b == machine['p'][0], 'X_Target'
		problem += machine['a'][1] * a + machine['b'][1] * b == machine['p'][1], 'Y_Target'
		problem += cost
		status = problem.solve(PULP_CBC_CMD(msg=0))
		if status == 1:
			# print(f'A Presses: {int(a.varValue)}, B Presses: {int(b.varValue)}, Cost: {int(cost.value())}')
			tokens += int(cost.value())
	return tokens

def part_2(machines):
	tokens = 0
	for machine in machines:
		machine['p'] = (machine['p'][0] + 10000000000000, machine['p'][1] + 10000000000000)

	for machine in machines:
		problem = LpProblem('Minimize_Button_Cost_2', LpMinimize)
		a = LpVariable('a', lowBound=100)
		b = LpVariable('b', lowBound=100)
		cost = 3 * a + 1 * b
		problem += machine['a'][0] * a + machine['b'][0] * b == machine['p'][0], 'X_Target'
		problem += machine['a'][1] * a + machine['b'][1] * b == machine['p'][1], 'Y_Target'
		problem += cost
		status = problem.solve(PULP_CBC_CMD(msg=0))
		if status == 1:
			# print(f'A Presses: {int(a.varValue)}, B Presses: {int(b.varValue)}, Cost: {int(cost.value())}')
			tokens += int(cost.value())
	return tokens

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
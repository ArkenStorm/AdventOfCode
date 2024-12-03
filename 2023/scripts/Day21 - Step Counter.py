import numpy as np
from collections import deque

# inFile = open('../inputs/Day21.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2023/inputs/Day21.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

grid = np.array([list(line) for line in lines])

print('Day 21 - Step Counter')

# Part 1
reachable_plots = 0
visited = set()

start = np.argwhere(grid == 'S')
steps, pos = 0, tuple(start[0])

max_steps = 64  # real
# max_steps = 6  # test

def bfs(matrix, start, max_steps):
	global reachable_plots

	q = deque([(start, 0)])

	while q:
		pos, curr_steps = q.popleft()
		if (pos, curr_steps) in visited or curr_steps > max_steps:
			continue
		visited.add((pos, curr_steps))
		if curr_steps == max_steps:
			reachable_plots += 1
			continue

		rows, cols = len(matrix), len(matrix[0])
		neighbors = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
		neighbors = list(filter(lambda c: 0 <= c[0] < rows and 0 <= c[1] < cols and matrix[c] != '#', neighbors))

		for n in neighbors:
			q.append((n, curr_steps + 1))

bfs(grid, tuple(start[0]), 64)

print(f"Part 1: {reachable_plots}")

# Part 2
expanded_grid = np.array([
	[
		grid[i % len(grid), j % len(grid[0])]
		for j in range(5 * len(grid[0]))
	]
	for i in range(5 * len(grid))
])

start = np.argwhere(grid == 'S')
# solve system of equations
# y = ax**2 + bx + c

y_vals = []
# 65 is steps to the edge of the first grid, then 131 is the length of the grid so we need 65 + 131, 65 + 131*2
for step_count in [65, 196, 327]:
	reachable_plots = 0
	visited.clear()
	bfs(expanded_grid, tuple(start[0]), step_count)
	y_vals.append(reachable_plots)

target = (26501365 - 65) // 131  # gets the number of grids we need to traverse
plots = np.round(np.polyval(np.polyfit([0, 1, 2], y_vals, 2), target), 0)

print(f"Part 2: {plots}")
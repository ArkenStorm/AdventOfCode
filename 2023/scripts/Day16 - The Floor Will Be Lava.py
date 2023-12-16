from functools import reduce
import numpy as np
from collections import deque
import sys
sys.setrecursionlimit(10000)

# inFile = open('../inputs/Day16.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2023/inputs/Day16.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

grid = [list(line) for line in lines]
energy_grid = [[False for _ in range(len(line))] for line in lines]
dirs = { (-1,0): 'n', (0,1): 'e', (1,0): 's', (0,-1): 'w' }
n, e, s, w = (-1, 0), (0, 1), (1, 0), (0, -1)

print('Day 16 - The Floor Will Be Lava')

seen = set()

# Part 1
# def trace_path(pos: tuple, dir: tuple):
# 	paths = deque([(pos, dir)])
# 	curr_energy = 0
# 	seen.clear()
# 	while len(paths) > 0:
# 		pos, dir = paths.popleft()
# 		if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]) or (pos, dir) in seen:
# 			continue

# 		seen.add((pos, dir))
# 		if energy_grid[pos[0]][pos[1]] != True:
# 			energy_grid[pos[0]][pos[1]] = True
# 			curr_energy += 1

# 		if grid[pos[0]][pos[1]] == '.':
# 			paths.append((tuple(np.add(pos, dir)), dir))
# 		elif grid[pos[0]][pos[1]] == '/':
# 			if dir == n:
# 				paths.append((tuple(np.add(pos, e)), e))
# 			elif dir == e:
# 				paths.append((tuple(np.add(pos, n)), n))
# 			elif dir == s:
# 				paths.append((tuple(np.add(pos, w)), w))
# 			else:
# 				paths.append((tuple(np.add(pos, s)), s))
# 		elif grid[pos[0]][pos[1]] == '\\':
# 			if dir == n:
# 				paths.append((tuple(np.add(pos, w)), w))
# 			elif dir == e:
# 				paths.append((tuple(np.add(pos, s)), s))
# 			elif dir == s:
# 				paths.append((tuple(np.add(pos, e)), e))
# 			else:
# 				paths.append((tuple(np.add(pos, n)), n))
# 		elif grid[pos[0]][pos[1]] == '|':
# 			if dirs[dir] in 'we':
# 				paths.append((tuple(np.add(pos, n)), n))
# 				paths.append((tuple(np.add(pos, s)), s))
# 			else:
# 				paths.append((tuple(np.add(pos, dir)), dir))
# 		elif grid[pos[0]][pos[1]] == '-':
# 			if dirs[dir] in 'ns':
# 				paths.append((tuple(np.add(pos, e)), e))
# 				paths.append((tuple(np.add(pos, w)), w))
# 			else:
# 				paths.append((tuple(np.add(pos, dir)), dir))
# 	return curr_energy


# dir is which direction the beam is currently going

def trace_path(pos: tuple, dir: tuple, curr_energy: int):
	if (pos, dir) in seen or pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
		return curr_energy
	
	seen.add((pos, dir))
	if energy_grid[pos[0]][pos[1]] != True:
		energy_grid[pos[0]][pos[1]] = True
		curr_energy += 1

	if grid[pos[0]][pos[1]] == '.':
		return trace_path(tuple(np.add(pos, dir)), dir, curr_energy)
	elif grid[pos[0]][pos[1]] == '/':
		if dir == n:
			return trace_path(tuple(np.add(pos, e)), e, curr_energy)
		elif dir == e:
			return trace_path(tuple(np.add(pos, n)), n, curr_energy)
		elif dir == s:
			return trace_path(tuple(np.add(pos, w)), w, curr_energy)
		else:
			return trace_path(tuple(np.add(pos, s)), s, curr_energy)
	elif grid[pos[0]][pos[1]] == '\\':
		if dir == n:
			return trace_path(tuple(np.add(pos, w)), w, curr_energy)
		elif dir == e:
			return trace_path(tuple(np.add(pos, s)), s, curr_energy)
		elif dir == s:
			return trace_path(tuple(np.add(pos, e)), e, curr_energy)
		else:
			return trace_path(tuple(np.add(pos, n)), n, curr_energy)
	elif grid[pos[0]][pos[1]] == '|':
		if dirs[dir] in 'we':
			curr_energy += trace_path(tuple(np.add(pos, n)), n, 0)
			curr_energy += trace_path(tuple(np.add(pos, s)), s, 0)
			return curr_energy
		else:
			return trace_path(tuple(np.add(pos, dir)), dir, curr_energy)
	elif grid[pos[0]][pos[1]] == '-':
		if dirs[dir] in 'ns':
			curr_energy += trace_path(tuple(np.add(pos, e)), e, 0)
			curr_energy += trace_path(tuple(np.add(pos, w)), w, 0)
			return curr_energy
		else:
			return trace_path(tuple(np.add(pos, dir)), dir, curr_energy)
	return curr_energy

trace_path((0, 0), (0, 1), 0)

# print([['#' if c else '.' for c in r] for r in energy_grid])
energized = sum(map(sum, energy_grid))
print(f"Part 1: {energized}")

# Part 2
max_energy = energized
for r in [0, len(grid) - 1]:
	dir = s if r == 0 else n
	for c in range(len(grid[0])):
		energy_grid = [[False for _ in range(len(line))] for line in lines]
		seen.clear()
		max_energy = max(max_energy, trace_path((r, c), dir, 0))

for c in [0, len(grid[0]) - 1]:
	dir = e if c == 0 else w
	for r in range(len(grid[0])):
		energy_grid = [[False for _ in range(len(line))] for line in lines]
		seen.clear()
		max_energy = max(max_energy, trace_path((r, c), dir, 0))

print(f"Part 2: {max_energy}")
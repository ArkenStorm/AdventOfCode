import numpy as np
from functools import reduce
import sys
sys.setrecursionlimit(10000)

inFile = open('../inputs/Day16.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day16.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

grid = [list(line) for line in lines]
energy_grid = [[False for _ in range(len(line))] for line in lines]
n, e, s, w = (-1, 0), (0, 1), (1, 0), (0, -1)

print('Day 16 - The Floor Will Be Lava')

seen = set()

# Part 1
mirrors = {
	'.': { n: [n], e: [e], s: [s], w: [w] },
	'/': { n: [e], e: [n], s: [w], w: [s] },
	'\\': { n: [w], e: [s], s: [e], w: [n] },
	'|': { n: [n], e: [n, s], s: [s], w: [n, s] },
	'-': { n: [e, w], e: [e], s: [e, w], w: [w] }
}

# dir is which direction the beam is currently going
def trace_path(pos: tuple, dir: tuple, curr_energy: int):
	if (pos, dir) in seen or pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
		return curr_energy
	
	seen.add((pos, dir))
	if not energy_grid[pos[0]][pos[1]]:
		energy_grid[pos[0]][pos[1]] = True
		curr_energy += 1

	nxt = mirrors[grid[pos[0]][pos[1]]][dir]
	# curr_energy = reduce(lambda acc, nxt_dir: acc + trace_path(tuple(np.add(pos, nxt_dir)), nxt_dir, 0), nxt, 0)
	for nxt_dir in nxt:
		nxt_pos = tuple(np.add(pos, nxt_dir))
		curr_energy += trace_path(nxt_pos, nxt_dir, 0)
	return curr_energy

trace_path((0, 0), (0, 1), 0)

# print([['#' if c else '.' for c in r] for r in energy_grid])
energized = sum(map(sum, energy_grid))
print(f"Part 1: {energized}")

# Part 2
max_energy = energized

tests = (
	[((r, 0), e) for r in range(len(grid))] +
	[((r, len(grid[0]) - 1), w) for r in range(len(grid))] +
	[((0, c), s) for c in range(len(grid[0]))] +
	[((len(grid) - 1, c), n) for c in range(len(grid[0]))]
)


for pos, dir in tests:
	energy_grid = [[False for _ in range(len(line))] for line in lines]
	seen.clear()
	max_energy = max(max_energy, trace_path(pos, dir, 0))

print(f"Part 2: {max_energy}")
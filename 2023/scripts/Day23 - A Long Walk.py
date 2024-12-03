import sys
sys.setrecursionlimit(10000)

# inFile = open('../inputs/Day23.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day23.txt')
inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

grid = [list(line) for line in lines]

print('Day 23 - A Long Walk')

# Part 1
path_lens = [2222]
start, end = (0, 1), (len(grid) - 1, len(grid[0]) - 2)
n, e, s, w = (-1, 0), (0, 1), (1, 0), (0, -1)
slopes = { '^': n, '>': e, 'v': s, '<': w }

def get_dirs(pos, path):
	dirs = [(pos[0] + d[0], pos[1] + d[1]) for d in [n, e, s, w]]
	dirs = list(filter(
		lambda d: d not in path and 0 <= d[0] < len(grid) and 0 <= d[1] < len(grid[0]) and grid[d[0]][d[1]] != '#',
		dirs
	))
	return dirs

def dfs(pos, path: set, use_slopes=True):
	if pos == end:
		path_lens.append(len(path) - 1)
		return
	if use_slopes:
		if (sl := grid[pos[0]][pos[1]]) in '^>v<':
			new_pos = (pos[0] + slopes[sl][0], pos[1] + slopes[sl][1])
			if new_pos not in path:
				path.add(new_pos)
				dfs(new_pos, path, use_slopes)
			return

	for d in get_dirs(pos, path):
		new_path = path.copy()
		new_path.add(d)
		dfs(d, new_path, use_slopes)

# dfs(start, set([start]))

print(f"Part 1: {max(path_lens)}")

# Part 2
graph = {}

def make_adjacency_graph():
	for i in range(len(grid)):
		for j in range(len(grid)):
			pos = (i, j)
			if grid[i][j] != '#':
				adjacent = {}
				for p in get_dirs(pos, set()):
					if grid[p[0]][p[1]] != '#':
						adjacent[p] = 1
				graph[pos] = adjacent

	keys = list(graph.keys())
	for key in keys:
		ns = graph[key]
		if len(ns) == 2:
			l, r = ns.keys()
			del graph[l][key]
			del graph[r][key]
			graph[l][r] = max(graph[l].get(r, 0), ns[l] + ns[r])
			graph[r][l] = graph[l][r]
			del graph[key]

def dfs_adj(pos, path: dict):
	if pos == end:
		path_lens.append(sum(path.values()))
		return

	for n in graph[pos]:
		if n in path:
			continue
		path[n] = graph[pos][n]
		dfs_adj(n, path)
		del path[n]

path_lens = []

make_adjacency_graph()

dfs_adj(start, { start: 0 })

print(f"Part 2: {max(path_lens)}")
import heapq as hq

inFile = open('../inputs/Day17.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day17.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

grid = [list(map(int, line)) for line in lines]
n, e, s, w = (-1, 0), (0, 1), (1, 0), (0, -1)
dirs = [n, e, s, w]
inverses = { n: s, e: w, s: n, w: e }

print('Day 17 - Clumsy Crucible')

# Part 1
min_heat_loss = float('inf')

queue = [(0, 1, (0,0), e), (0, 1, (0,0), s)]
hq.heapify(queue)

def dijkstra(q: list, min_streak=1, max_streak=3):
	global min_heat_loss

	path = set()
	while len(q) > 0:
		curr_loss, streak, pos, dir = hq.heappop(q)
		if (pos, dir, streak) in path:
			continue
		path.add((pos, dir, streak))
		for new_dir in dirs:
			new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
			new_streak = streak + 1 if new_dir == dir else 1
			if (
				not 0 <= new_pos[0] < len(grid) or
				not 0 <= new_pos[1] < len(grid[0]) or
				new_dir == inverses[dir] or
				(new_dir != dir and streak < min_streak) or
				(new_dir == dir and streak == max_streak) or
				(new_pos, new_dir, new_streak) in path
			):
				continue
			new_loss = curr_loss + grid[new_pos[0]][new_pos[1]]
			if new_pos == (len(grid) - 1, len(grid[0]) - 1):
				min_heat_loss = min(min_heat_loss, new_loss)
			hq.heappush(q, (new_loss, new_streak, new_pos, new_dir))

dijkstra(queue)

print(f"Part 1: {min_heat_loss}")

# Part 2
queue = [(0, 1, (0,0), e), (0, 1, (0,0), s)]
hq.heapify(queue)
min_heat_loss = float('inf')

dijkstra(queue, 4, 10)

print(f"Part 2: {min_heat_loss}")
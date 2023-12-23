from collections import defaultdict

inFile = open('../inputs/Day22.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day22.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 22 - Sand Slabs')

# Part 1
bricks = []
for line in lines:
	a, b = line.split('~')
	bricks.append([list(map(int, a.split(','))), list(map(int, b.split(',')))])

# so I have to make the bricks fall, and then figure out which bricks are supported by 2 or more
# sort bricks by height

bricks = sorted(bricks, key=lambda b: b[0][2])
dep_graph = [[] for _ in range(len(bricks))] # part 2
invalid = set()

def drop_bricks():
	highest = defaultdict(lambda: (0, -1))  # (x, y) -> (z, idx)

	for idx, b in enumerate(bricks):
		max_height = -1
		supports = set()
		for x in range(b[0][0], b[1][0] + 1):
			for y in range(b[0][1], b[1][1] + 1):
				if highest[x,y][0] + 1 > max_height:
					max_height = highest[x,y][0] + 1
					supports = { highest[x,y][1] }
				elif highest[x,y][0] + 1 == max_height:
					supports.add(highest[x,y][1])

		for s in set(filter(lambda x: x != -1, supports)):
			dep_graph[s].append(idx)

		if len(supports) == 1:
			invalid.add(supports.pop())

		if (fall_dist := b[0][2] - max_height) > 0:
			b[0][2] -= fall_dist
			b[1][2] -= fall_dist

		for x in range(b[0][0], b[1][0] + 1):
			for y in range(b[0][1], b[1][1] + 1):
				highest[x, y] = (b[1][2], idx)

drop_bricks()

disintegratable = len(bricks) - (len(invalid) - 1)

print(f"Part 1: {disintegratable}")

# Part 2
def chain_reaction(idx):
	in_deg = [0 for _ in range(len(bricks))]
	for i in range(len(bricks)):
		for j in dep_graph[i]:
			in_deg[j] += 1

	q = [idx]
	count = -1
	while len(q) > 0:
		count += 1
		x = q.pop()
		for i in dep_graph[x]:
			in_deg[i] -= 1
			if in_deg[i] == 0:
				q.append(i)
	return count

total_affected = sum(chain_reaction(i) for i in range(len(bricks)))

print(f"Part 2: {total_affected}")
from functools import reduce
from matplotlib.path import Path
from shapely import Polygon

# inFile = open('../inputs/Day18.txt', 'r')
inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day18.txt', 'r')
# inFile = open('2023/inputs/test.txt', 'r')
lines = [line.split() for line in inFile.read().splitlines()]

u, r, d, l = (-1, 0), (0, 1), (1, 0), (0, -1)
dirs = { 'U': u, 'R': r, 'D': d, 'L': l }

print('Day 18 - Lavaduct Lagoon')

p1_vertices, p1_area = [(0,0)], 0
p2_vertices, p2_area = [(0,0)], 0

for dir, dist, color in lines:
	p1_vertices.append()
	pass


# Part 1
pos = (0, 0)
path = [pos]
perimeter = 0
area = 0
colors = []

for line in lines:
	dir, dist, color = line.split()
	dist = int(dist)
	color = color[2:-1]
	colors.append(color)
	perimeter += dist

	for i in range(1, dist + 1):
		nxt_pos = (pos[0] + dirs[dir][0] * i, pos[1] + dirs[dir][1] * i)
		path.append(nxt_pos)
	pos = nxt_pos
	# pos = (pos[0] + dirs[dir][0] * dist, pos[1] + dirs[dir][1] * dist)
	# path.append(pos)

area += perimeter

min_x, min_y = min(path, key=lambda p: p[0])[0], min(path, key=lambda p: p[1])[1]
max_x, max_y = max(path, key=lambda p: p[0])[0], max(path, key=lambda p: p[1])[1]
size_x, size_y = abs(max_x - min_x) + 1, abs(max_y - min_y) + 1

# grid = [['#' if (x, y) in path else '.' for y in range(size_y + 1)] for x in range(size_x + 1)]
vertices = set(path)
polygon = Path(path)
for x in range(min_x, size_x):
	for y in range(min_y, size_y):
		if polygon.contains_point((x, y)) and (x, y) not in vertices:
			area += 1

# reductor = lambda acc, coord: acc + 1 if coord not in vertices and polygon.contains_point(coord) else acc
# reduce(reductor, ((x, y) for x in range(size_x) for y in range(size_y)), area)

print(f"Part 1: {area}")

# Part 2
dig_codes = { '0': r, '1': d, '2': l, '3': u }
pos = (0, 0)
path = [(0, 0)]
perimeter = 0
area = 0
for color in colors:
	dist, dir = int(color[:-1], 16), color[-1]
	perimeter += dist
	# pos = (pos[0] + dig_codes[dir][0] * dist, pos[1] + dig_codes[dir][1] * dist)
	# path.append(pos)
	for i in range(1, dist + 1):
		nxt_pos = (pos[0] + dig_codes[dir][0] * i, pos[1] + dig_codes[dir][1] * i)
		path.append(nxt_pos)
	pos = nxt_pos

area += perimeter

min_x, min_y = min(path, key=lambda p: p[0])[0], min(path, key=lambda p: p[1])[1]
max_x, max_y = max(path, key=lambda p: p[0])[0], max(path, key=lambda p: p[1])[1]
size_x, size_y = abs(max_x - min_x) + 1, abs(max_y - min_y) + 1

# grid = [['#' if (x, y) in path else '.' for y in range(size_y + 1)] for x in range(size_x + 1)]
# vertices = set(path)
# polygon = Path(path)
# for x in range(min_x, size_x):
# 	for y in range(min_y, size_y):
# 		if polygon.contains_point((x, y)) and (x, y) not in vertices:
# 			area += 1

print(f"Part 2: {area}")
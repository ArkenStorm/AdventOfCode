from matplotlib.path import Path
from shapely import Polygon

inFile = open('../inputs/Day18.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
# inFile = open('2023/inputs/Day18.txt', 'r')
# inFile = open('2023/inputs/test.txt', 'r')
lines = [line.split() for line in inFile.read().splitlines()]

u, r, d, l = (-1, 0), (0, 1), (1, 0), (0, -1)
dirs = { 'U': u, 'R': r, 'D': d, 'L': l }
dig_codes = { '0': r, '1': d, '2': l, '3': u }

print('Day 18 - Lavaduct Lagoon')

p1_vertices, p1_area = [(0,0)], 0
p2_vertices, p2_area = [(0,0)], 0

for dir, dist, color in lines:
	# Part 1
	pos = p1_vertices[-1]
	p1_vertices.append((pos[0] + dirs[dir][0] * int(dist), pos[1] + dirs[dir][1] * int(dist)))

	# Part 2
	pos = p2_vertices[-1]
	dir = color[-2]
	dist = int(color[2:-2], 16)
	p2_vertices.append((pos[0] + dig_codes[dir][0] * dist, pos[1] + dig_codes[dir][1] * dist))

p1 = int(Polygon(p1_vertices).buffer(0.5, join_style='mitre').area)
p2 = int(Polygon(p2_vertices).buffer(0.5, join_style='mitre').area)
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
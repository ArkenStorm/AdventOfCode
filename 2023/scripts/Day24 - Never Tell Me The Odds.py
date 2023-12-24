import numpy as np
from itertools import combinations
from z3 import BitVec, Solver

# inFile = open('../inputs/Day24.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2023/inputs/Day24.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

hailstones = []
for line in lines:
	pos, v = line.split(' @ ')
	pos, v = np.array(list(map(int, pos.split(', ')))), np.array(list(map(int, v.split(', '))))
	hailstones.append((pos, v))

print('Day 24 - Never Tell Me The Odds')

# Part 1
intersections = 0
# bounds = (7, 27)  # test
bounds = (200000000000000, 400000000000000)  # real

# this has an off-by-one: gets 12341 but should get 12343
# for i in range(len(hailstones)):
# 	a1, v1 = hailstones[i]
# 	A = np.array([a1[:2], a1[:2] + v1[:2]])
# 	for j in range(i + 1, len(hailstones)):
# 		b1, v2 = hailstones[j]
# 		B = np.array([b1[:2], b1[:2] + v2[:2]])
# 		try:
# 			t, s = np.linalg.solve(np.array([A[1] - A[0], B[0] - B[1]]).T, B[0] - A[0])
# 			a_i_pt = (1-t) * A[0] + t * A[1]
# 			b_i_pt = (1-s) * B[0] + s * B[1]
# 			if (
# 				bounds[0] <= a_i_pt[0] <= bounds[1] and
# 				bounds[0] <= a_i_pt[1] <= bounds[1] and
# 				bounds[0] <= b_i_pt[0] <= bounds[1] and
# 				bounds[0] <= b_i_pt[1] <= bounds[1] and
# 				t > 0 and s > 0
# 			):
# 				intersections += 1
# 		except:
# 			# no solution to intersection
# 			continue

for h1, h2 in combinations(hailstones, 2):
	(x1, y1, _), (vx1, vy1, _) = h1
	(x2, y2, _), (vx2, vy2, _) = h2
	m1, m2 = vy1 / vx1, vy2 / vx2  # slopes
	if m1 == m2:
		continue  # parallel, we don't care
	A = np.array([[m1, -1], [m2, -1]])
	B = np.array([m1 * x1 - y1, m2 * x2 - y2])
	x, y = np.linalg.solve(A, B)

	t1 = (x - x1) / vx1
	t2 = (x - x2) / vx2
	if bounds[0] <= x <= bounds[1] and bounds[0] <= y <= bounds[1] and t1 > 0 and t2 > 0:
		intersections += 1

print(f"Part 1: {intersections}")

# Part 2

solver = Solver()
x, y, z, vx, vy, vz = (BitVec(name, 64) for name in ('x', 'y', 'z', 'vx', 'vy', 'vz'))
for i in range(len(hailstones)):
	pos, hv = hailstones[i]
	t = BitVec(f"t{i}", 64)
	solver.add(x + vx * t == pos[0] + hv[0] * t)
	solver.add(y + vy * t == pos[1] + hv[1] * t)
	solver.add(z + vz * t == pos[2] + hv[2] * t)
	solver.add(t > 0)
solver.check()
m = solver.model()

magic_point = m.eval(x + y + z)

print(f"Part 2: {magic_point}")
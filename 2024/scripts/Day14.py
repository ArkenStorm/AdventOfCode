from utils import *
from datetime import datetime
from collections import defaultdict, Counter
from math import prod

# coordinate -> count of robots at that coordinate
positions = defaultdict(int)

def get_positions(robots, time, board_width, board_height):
	positions.clear()
	for bot in robots:
		new_x = (bot['pos'][0] + (time * bot['vel'][0])) % board_width
		new_y = (bot['pos'][1] + (time * bot['vel'][1])) % board_height
		positions[(new_x, new_y)] += 1

def part_1(robots, board_width, board_height):
	get_positions(robots, 100, board_width, board_height)
	quadrants = Counter()
	for pos, count in positions.items():
		if pos[0] == board_width // 2 or pos[1] == board_height // 2:
			continue
		quadrants[(pos[0] < board_width // 2, pos[1] < board_height // 2)] += count
	return prod(quadrants.values())

def dfs(board, x, y, visited, bw, bh):
	visited.add((x, y))
	count = 1
	for coord in filter(lambda c: c in positions and c not in visited, get_bounded_4_neighbors(board, x, y)):
		count += dfs(board, *coord, visited, bw, bh)
	return count


def get_contiguous_size(bw, bh):
	counts = []
	visited = set()
	board = [[0] * bw for _ in range(bh)]
	counts = [dfs(board, *pos, visited, bw, bh) for pos in positions]
	return max(counts)

def part_2(robots, board_width, board_height):
	time = 0
	while time < (101  * 103):
		time += 1
		get_positions(robots, time, board_width, board_height)
		if get_contiguous_size(board_width, board_height) >= 30:
			break
	return time

def main(year, day):
	print(f'Day {day} - Restroom Redoubt')

	input = get_input(year, day, test=False)

	# board_width, board_height = 11, 7
	board_width, board_height = 101, 103
	robots = []

	for line in input:
		line = line.split(' ')
		x, y = map(int, line[0][2:].split(','))
		vx, vy = map(int, line[1][2:].split(','))
		robots.append({'pos': (x, y), 'vel': (vx, vy)})

	p1_start = datetime.now()
	print(f'Part 1: {part_1(robots, board_width, board_height)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(robots, board_width, board_height)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
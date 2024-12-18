from utils import *
from datetime import datetime
import heapq as hq

# change these for real vs test input
byte_chunk = 1024
end = (70, 70)

def find_exit(bytefall):
	checked = set()
	q = [(0, (0, 0))] # steps, (x, y)
	hq.heapify(q)
	while len(q) > 0:
		steps, coord = hq.heappop(q)
		if coord in checked:
			continue
		checked.add(coord)
		if coord == end:
			return steps
		for nx, ny in apply_deltas_4(*coord):
			if (nx, ny) in bytefall or nx < 0 or nx > end[0] or ny < 0 or ny > end[1]:
				continue
			hq.heappush(q, (steps + 1, (nx, ny)))
	return None

def part_1(all_bytes):
	bytefall = set(all_bytes[:byte_chunk])
	return find_exit(bytefall)

def part_2(all_bytes):
	low_limit, hi_limit = 0, len(all_bytes)
	byte_range = len(all_bytes) // 2
	while low_limit != hi_limit - 1:
		bytefall = set(all_bytes[:byte_range])
		if find_exit(bytefall) is not None:
			low_limit = byte_range
		else:
			hi_limit = byte_range
		byte_range = (hi_limit + low_limit) // 2
	return all_bytes[low_limit]

def main(year, day):
	print(f'Day {day} - RAM Run')

	input = get_input(year, day, test=False)
	all_bytes = list(map(lambda b: tuple(map(int, b.split(','))), input))

	p1_start = datetime.now()
	print(f'Part 1: {part_1(all_bytes)}')
	p1_end = datetime.now()

	p2_start = datetime.now()
	print(f'Part 2: {part_2(all_bytes)}')
	p2_end = datetime.now()

	print(f'\nExecution Times:\n\tPart 1: {p1_end - p1_start}\n\tPart 2: {p2_end - p2_start}\n')
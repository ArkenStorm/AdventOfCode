from functools import reduce

inFile = open('../inputs/Day6.txt', 'r')
lines = inFile.read().splitlines()

print('Day 6 - Wait For It')

times = list(map(int, lines[0][5:].split()))
distances = list(map(int, lines[1][9:].split()))

def ways_to_beat_race(time, dist):
	return sum(1 for i in range(1, time) if i* time - 1 > dist)

# Part 1
final = reduce(lambda acc, idx: acc * ways_to_beat_race(times[idx], distances[idx]), range(len(times)), 1)

print(f"Part 1: {final}")

# Part 2
time = int(''.join(lines[0][5:].split()))
dist = int(''.join(lines[1][9:].split()))

wins = ways_to_beat_race(time, dist)

print(f"Part 2: {wins}")
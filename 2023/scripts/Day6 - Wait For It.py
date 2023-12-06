inFile = open('../inputs/Day6.txt', 'r')
lines = inFile.read().splitlines()

print('Day 6 - Wait For It')

times = list(map(int, lines[0][5:].split()))
distances = list(map(int, lines[1][9:].split()))

def find_ways_to_beat_race(time, dist):
	ways_to_beat_race = 0
	for i in range(1, time):
		if i * time - i > dist:
			ways_to_beat_race += 1
	return ways_to_beat_race

# Part 1
final = 1

for i in range(len(times)):
	final *= find_ways_to_beat_race(times[i], distances[i])

print(f"Part 1: {final}")

# Part 2
time = int(''.join(lines[0][5:].split()))
dist = int(''.join(lines[1][9:].split()))

ways_to_beat_race = find_ways_to_beat_race(time, dist)

print(f"Part 2: {ways_to_beat_race}")
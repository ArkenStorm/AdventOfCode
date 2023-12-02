import re

inFile = open('../inputs/Day2.txt', 'r')
lines = inFile.read().splitlines()

print('Day 2 - Cube Conundrum')

# Part 1
maxes = {
	'red': 12,
	'green': 13,
	'blue': 14,
}

impossible = []

for line in lines:
	game, subsets = line.split(': ')
	game_id = re.match(r"Game (\d+)", game).group(1)
	draws = re.findall(r"(?:(?:(\d+) (?:(green|red|blue)(?:, )?){1,3})(?:; )?)", subsets)
	impossible.extend(game_id for val, color in draws if int(val) > maxes[color] and game_id not in impossible)

# print(impossible)
print(f"Part 1: {sum(map(int, impossible))}")

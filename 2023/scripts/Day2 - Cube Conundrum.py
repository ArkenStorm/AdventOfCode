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

impossible = set()
possible = set(range(1, 101))

for line in lines:
	game, subsets = line.split(': ')
	game_id = int(re.match(r"Game (\d+)", game).group(1))
	draws = re.findall(r"(?:(?:(\d+) (?:(green|red|blue)(?:, )?){1,3})(?:; )?)", subsets)
	impossible.update(game_id for val, color in draws if int(val) > maxes[color])

possible = possible - impossible
print(f"Part 1: {sum(possible)}")


# Part 2
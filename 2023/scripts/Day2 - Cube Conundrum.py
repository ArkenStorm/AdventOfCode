import re

inFile = open('../inputs/Day2.txt', 'r')
games = inFile.read().splitlines()

print('Day 2 - Cube Conundrum')

subset_re = r"(?:(?:(\d+) (?:(green|red|blue)(?:, )?){1,3})(?:; )?)"

# Part 1
maxes = { 'red': 12, 'green': 13, 'blue': 14 }

impossible = set()
possible = set(range(1, 101))

for game in games:
	game_id = int(re.match(r"Game (\d+)", game).group(1))
	draws = re.findall(subset_re, game)
	impossible.update(game_id for val, color in draws if int(val) > maxes[color])

possible = possible - impossible
print(f"Part 1: {sum(possible)}")

# doesn't quite work, but oh well
# test = set(range(1, 101)) - {int(re.match(r"Game (\d+)", game).group(1)) for val, color in re.findall(r'(?:(?:(\d+) (?:(green|red|blue)(?:, )?){1,3})(?:; )?)', game) if int(val) > maxes[color] for game in games}

# Part 2
power_total = 0

for game in games:
	mins = { 'red': 0, 'green': 0, 'blue': 0 }
	draws = re.findall(subset_re, game)
	for val, color in draws:
		if int(val) > mins[color]:
			mins[color] = int(val)
	power_total += mins['red'] * mins['green'] * mins['blue']

print(f"Part 2: {power_total}")
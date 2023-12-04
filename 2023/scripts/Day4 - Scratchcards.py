inFile = open('../inputs/Day4.txt', 'r')
cards = inFile.read().splitlines()

print('Day 4 - Scratchcards')

# Part 1
point_total = 0
amount_of_copies = dict([(i, 1) for i in range(len(cards))])

for i in range(len(cards)):
	winning, personal = cards[i][9:].split('|')
	matches = set(map(int, winning.split())).intersection(set(map(int, personal.split())))
	if len(matches) > 0:
		point_total += 2**(len(matches) - 1)
	for j in range(amount_of_copies[i]):
		for x in range(len(matches)):
			amount_of_copies[i+x+1] += 1

print(f"Part 1: {point_total}")

# Part 2
print(f"Part 2: {sum(amount_of_copies.values())}")
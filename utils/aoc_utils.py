def get_input(year, day_num, type='default', test=False):
	inFile = open(f"{year}/inputs/{'test' if test else f'Day{day_num}'}.txt", 'r')
	if type == 'default':
		return inFile.read().splitlines()
	elif type == 'grid':
		return [list(line) for line in inFile.read().splitlines()]
	else:
		return inFile.read()
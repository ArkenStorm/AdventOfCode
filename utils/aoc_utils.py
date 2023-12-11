def get_input(year, day_num, test=False):
	inFile = open(f"{year}/inputs/{'test' if test else f'Day{day_num}'}", 'r')
	return inFile.read().splitlines()
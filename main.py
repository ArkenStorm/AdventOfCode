from importlib import import_module
import shutil
from datetime import datetime

if __name__ == '__main__':
	year = 2024
	day = 17

	print(f'Advent of Code {year}')

	try:
		module = import_module(f'{year}.scripts.Day{day}')
		start_time = datetime.now()
		module.main(year, day)
		print(f'Total Execution Time: {datetime.now() - start_time}')
	except ModuleNotFoundError:
		print(f'No module found for Day {day}, creating...')
		shutil.copy('template.py', f'{year}/scripts/Day{day}.py')
		open(f'{year}/inputs/Day{day}.txt', 'w').close()
		print(f'Created Day{day}.py for {year}')
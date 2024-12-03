from importlib import import_module
import shutil

if __name__ == '__main__':
	year = 2024
	day = 2

	print(f'Advent of Code {year}')

	try:
		module = import_module(f'{year}.scripts.Day{day}')
		module.main(year, day)
	except ModuleNotFoundError:
		print(f'No module found for Day {day}, creating...')
		shutil.copy('template.py', f'{year}/scripts/Day{day}.py')
		print(f'Created Day{day}.py for {year}')
		exit()
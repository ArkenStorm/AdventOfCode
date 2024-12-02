# imports
# import import_module, util from importlib
from aoc_utils import get_input

if __name__ == '__main__':
	year = 2024
	day = 1

	print(f'Advent of Code {year}')
	# The idea here is to have a main file that will call the functions from the other files
	# Every file should export its logic as a function that will be called from here
	# This way we can keep the main file clean and organized
	# all the printing and formatting should be done here

	# I want to be able to just change the day and year number and run this file to get the results

	# dynamically import the module for the current day if it exists
	# found = util.find_spec(f'Day{day}', package=f'{year}.scripts')
	# if found:
	# 	module = import_module(f'{year}.scripts.Day{day}')
	# else:
	# 	print(f'No module found for Day {day}')
	# 	exit()
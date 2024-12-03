from collections import deque

inFile = open('../inputs/Day5.txt', 'r')
lines = inFile.read().splitlines()

print('Day 5 - If You Give A Seed A Fertilizer')

# Part 1
seeds = lines[0][6:].split()

# destination, source, range
seed_to_soil = [mapping.split() for mapping in lines[3:46]]
soil_to_fertilizer = [mapping.split() for mapping in lines[48:61]]
fertilizer_to_water = [mapping.split() for mapping in lines[63:108]]
water_to_light = [mapping.split() for mapping in lines[110:145]]
light_to_temperature = [mapping.split() for mapping in lines[147:160]]
temperature_to_humidity = [mapping.split() for mapping in lines[162:196]]
humidity_to_location = [mapping.split() for mapping in lines[198:]]

map_chain = [
	seed_to_soil,
	soil_to_fertilizer,
	fertilizer_to_water,
	water_to_light,
	light_to_temperature,
	temperature_to_humidity,
	humidity_to_location,
]

min_location = 9999999999999

def get_next_mapping(source, mapping):
	for line in mapping:
		dest, src, rng = int(line[0]), int(line[1]), int(line[2])
		if source in range(src, src + rng):
			return dest + (source - src)
	return source

for seed in seeds:
	# seed -> soil -> fertilizer -> water -> light -> temp -> humidity -> location
	soil = get_next_mapping(int(seed), seed_to_soil)
	fert = get_next_mapping(soil, soil_to_fertilizer)
	water = get_next_mapping(fert, fertilizer_to_water)
	light = get_next_mapping(water, water_to_light)
	temp = get_next_mapping(light, light_to_temperature)
	humidity = get_next_mapping(temp, temperature_to_humidity)
	location = get_next_mapping(humidity, humidity_to_location)

	min_location = min(location, min_location)

print(f"Part 1: {min_location}")

# Part 2
seed_ranges = list(zip(seeds[::2], seeds[1::2]))
stack = deque()
min_location = 9999999999999

for seed_range in seed_ranges:
	stack.append((seed_range, 0))  # ( (start, len), stage )

	while len(stack) > 0:
		curr_range, stage = stack.pop()

		if stage == len(map_chain):
			min_location = min(min_location, curr_range[0])
			continue

		curr_map = map_chain[stage]
		found_overlap = False

		for line in curr_map:
			dest, src, rng = int(line[0]), int(line[1]), int(line[2])
			curr_range_start = int(curr_range[0])
			curr_range_end = curr_range_start + int(curr_range[1])
			map_end = src + rng
			if curr_range_end < src or curr_range_start >= map_end:
				continue
			found_overlap = True
			if curr_range_start < src and curr_range_end > map_end: # source range encapsulates map range
				# split into 3 chunks of [start, end), [start, end], (start, end]
				stack.append( ((curr_range_start, src - curr_range_start), stage) )
				stack.append( ((dest, rng), stage + 1) )
				stack.append( ((map_end, curr_range_end - map_end), stage) )
			elif curr_range_start < src and src < curr_range_end <= map_end:
				stack.append( ((curr_range_start, src - curr_range_start), stage) )
				stack.append( ((dest, curr_range_end - src), stage + 1) )
			elif src <= curr_range_start < map_end and curr_range_end > map_end:
				stack.append( ((dest + (curr_range_start - src), map_end - curr_range_start), stage + 1) )
				stack.append( ((map_end, curr_range_end - map_end), stage) )
			else:
				stack.append( ((dest + (curr_range_start - src), int(curr_range[1])), stage + 1) )
			break
		if not found_overlap:
			stack.append((curr_range, stage + 1))


print(f"Part 2: {min_location}")
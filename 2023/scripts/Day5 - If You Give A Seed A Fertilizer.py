inFile = open('../inputs/Day5.txt', 'r')
lines = inFile.read().splitlines()

print('Day 5 - If You Give A Seed A Fertilizer')

# Part 1
seeds = lines[0][6:].split()

# destination, source, range
seed_to_soil = [mapping.split() for mapping in lines[4:46]]
soil_to_fertilizer = [mapping.split() for mapping in lines[49:61]]
fertilizer_to_water = [mapping.split() for mapping in lines[64:108]]
water_to_light = [mapping.split() for mapping in lines[111:145]]
light_to_temperature = [mapping.split() for mapping in lines[148:160]]
temperature_to_humidity = [mapping.split() for mapping in lines[163:196]]
humidity_to_location = [mapping.split() for mapping in lines[199:]]

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

print(f"Part 2: {min_location}")
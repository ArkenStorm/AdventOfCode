import queue
import math

# inFile = open('../inputs/Day20.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2023/inputs/Day20.txt')
# inFile = open('2023/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 20 - Pulse Propagation')

flips, cons, modules = {}, {}, {}

for line in lines:
	src, dests = line.split(' -> ')
	dests = dests.split(', ')
	key = 'broadcaster' if src == 'broadcaster' else src[1:]
	
	if src.startswith('%'):
		flips[src[1:]] = False
	elif src.startswith('&'):
		cons[src[1:]] = {}
	
	modules[key] = dests

for mod in modules:
	for dest in modules[mod]:
		if dest in cons:
			cons[dest][mod] = 'low'

# Part 1
signals = queue.Queue()
pulse_map = { 'high': 0, 'low': 0 }
presses = 0
# high pulse iterations
hpis = { mod: 0 for mod in cons['lg'] }

def send_pulses(src, mod, p_type):
	global pulse_map, presses

	if mod == 'lg' and p_type == 'high':
		hpis[src] = presses
		if all(hpis[i] > 0 for i in hpis):
			raise Exception

	if mod in flips and p_type == 'low':
		flip_p_type = 'low'
		if flips[mod]:
			flips[mod] = False
			flip_p_type = 'low'
		else:
			flips[mod] = True
			flip_p_type = 'high'
		
		for dest in modules[mod]:
			pulse_map[flip_p_type] += 1
			signals.put((mod, dest, flip_p_type))
	elif mod in cons:
		cons[mod][src] = p_type
		con_p_type = 'low' if all(p == 'high' for p in cons[mod].values()) else 'high'
		for dest in modules[mod]:
			pulse_map[con_p_type] += 1
			signals.put((mod, dest, con_p_type))

def push_button():
	global pulse_map

	for dest in modules['broadcaster']:
		signals.put(('broadcaster', dest, 'low'))
		pulse_map['low'] += 1
	while not signals.empty():
		send_pulses(*signals.get())

for _ in range(1000):
	pulse_map['low'] += 1
	push_button()

pulse_count = pulse_map['high'] * pulse_map['low']

print(f"Part 1: {pulse_count}")

# Part 2

# reset all modules
for mod in flips:
	flips[mod] = False
for mod in cons:
	for src in cons[mod]:
		cons[mod][src] = 'low'

try:
	while True:
		presses += 1
		push_button()
except:
	pass

min_button_presses = math.lcm(*hpis.values())

print(f"Part 2: {min_button_presses}")
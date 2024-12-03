# inFile = open('../inputs/Day2.txt', 'r')
# inFile = open('../inputs/test.txt', 'r')
inFile = open('2024/inputs/Day2.txt', 'r')
# inFile = open('2024/inputs/test.txt', 'r')
lines = inFile.read().splitlines()

print('Day 2 - Red-Nosed Reports')

# Part 1
lines = [list(map(int, line.split())) for line in lines]
p1_safe, p2_safe = 0, 0

is_safe = lambda arr: all(1 <= abs(x - y) <= 3 for x, y in zip(arr, arr[1:])) and (arr == sorted(arr) or arr == sorted(arr, reverse=True))

p1_safe = sum(map(is_safe, lines))

print(f'Part 1: {p1_safe}')

# Part 2
dampener = lambda arr: any(is_safe(arr[:i] + arr[i + 1:]) for i in range(len(arr)))

p2_safe = sum(map(dampener, lines))
print(f'Part 2: {p2_safe}')
import re
from functools import reduce

inFile = open('../inputs/Day1.txt', 'r')
lines = inFile.read().splitlines()

print("Day 1 - Trebuchet")

# Part 1
combine = lambda x: int(x[0] + x[-1])
getDigits = lambda l: re.findall(r"\d", l)

total = sum(map(combine, map(getDigits, lines)))
# total = sum(map(lambda x: int(x[0] + x[-1]), map(lambda l: re.findall(r"\d", l), lines)))
print(f"Part 1: {total}")


# Part 2
numMap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

newLines = []
for line in lines:
    for i in range(len(line)):
        for key in numMap:
            if line.startswith(key, i):
                line = line[:i + 1] + numMap[key] + line[i + 2:]
                break
    newLines.append(line)

# test = [line[:i + 1] + numMap[key] + line[i + 2:] if line.startswith(key, i) else line for i in range(len(line)) for line in lines]

total = sum(map(combine, map(getDigits, newLines)))
print(f"Part 2: {total}")

# total = sum(map(lambda x: int(x[0] + x[-1]), map(lambda l: re.findall(r"\d", l), [line[:i + 1] + numMap[key] + line[i + 2:] if line.startswith(key, i) else line for i in range(len(line)) for line in lines])))

# Part 2 alternate
numMap = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3ree",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "s7ven",
    "eight": "e8ght",
    "nine": "n9ne",
}

replaceWordNums = lambda line: reduce(lambda x, y: x.replace(y, numMap[y]), numMap, line)

total = sum(map(combine, map(getDigits, map(replaceWordNums, lines))))
print(f"Part 2 alternate: {total}")
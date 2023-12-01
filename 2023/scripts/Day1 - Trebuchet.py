import re

inFile = open('../inputs/Day1.txt', 'r')
lines = inFile.read().splitlines()

print("Day 1 - Trebuchet")

# Part 1
combine = lambda x: int(x[0] + x[-1])
getDigits = lambda l: re.findall(r"\d", l)

total = sum(map(combine, map(getDigits, lines)))
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

numStrings = tuple(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

newLines = []
for line in lines:
    for i in range(len(line)):
        for key in numMap:
            if line.startswith(key, i):
                # line = line.replace(key, numMap[key])
                line = line[:i + 1] + numMap[key] + line[i + 1:]
                break
    print(line)
    newLines.append(line)

total = sum(map(combine, map(getDigits, newLines)))
print(f"Part 2: {total}")
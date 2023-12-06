from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=2, width=120)

# Read the input file. The with statement automatically closes the file after the block
with open("3_in.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def getCommonChar(left, right):
    for char in left:
        if char in right:
            return char
    # return list(set(left).intersection(set(right)))[0]


def getPriority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


totalPriority = 0
for line in lines:
    left = line[0 : int(len(line) / 2)]
    right = line[int(len(line) / 2) : len(line)]
    totalPriority += getPriority(getCommonChar(left, right))
    # print("ASCII of " + common + " is ", ord(common))

print("Total priority of common items is", totalPriority)

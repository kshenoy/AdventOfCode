from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=2, width=120)


def getCommonItem(elfA, elfB, elfC):
    for item in elfA:
        if (item in elfB) and (item in elfC):
            return item


def getPriority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


# Read the input file. The with statement automatically closes the file after the block
with open("3_in.txt") as file:
    totalPriority = 0
    for elfA in file:
        elfB = next(file)
        elfC = next(file)
        totalPriority += getPriority(
            getCommonItem(elfA.strip(), elfB.strip(), elfC.strip())
        )

print(totalPriority)

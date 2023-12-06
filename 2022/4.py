import pprint

pp = pprint.PrettyPrinter(indent=2, width=120)


def makeSectionSets(input: str) -> set:
    begin, end = [int(i) for i in input.split("-")]
    return set(range(begin, end + 1))


def hasFullOverlap(assElfA: set, assElfB: set) -> bool:
    return assElfA.issubset(assElfB) or assElfB.issubset(assElfA)


def hasPartialOverlap(assElfA: set, assElfB: set) -> bool:
    return not assElfA.isdisjoint(assElfB)


fullOverlaps = 0
partialOverlaps = 0
with open("4_in.txt") as file:
    for line in file:
        assElfA, assElfB = [makeSectionSets(i) for i in line.strip().split(",")]
        fullOverlaps += hasFullOverlap(assElfA, assElfB)
        partialOverlaps += hasPartialOverlap(assElfA, assElfB)

print("FullOverlaps=", fullOverlaps, ", PartialOverlaps=", partialOverlaps, sep="")

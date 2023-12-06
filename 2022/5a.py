import pprint
import re

pp = pprint.PrettyPrinter(indent=2, width=120)


cratePosRegex = re.compile("\s*\[[A-Z]\]")
crateMoveRegex = re.compile("^move")

Model = 9001
tracker = {}


def getCratePos(stack: int) -> int:
    return 4 * stack - 3


def stackCrates(line: str):
    stack = 1
    cratePos = getCratePos(stack)
    while cratePos < len(line):
        crate = line[cratePos]
        if crate != " ":
            tracker.setdefault(stack, []).insert(0, crate)
        stack += 1
        cratePos = getCratePos(stack)


def moveCrates(src: int, dst: int, num: int):
    numCratesToBeMoved = min(num, len(tracker[src]))
    cratesToBeMoved = []
    if Model == 9000:
        for _ in range(numCratesToBeMoved):
            cratesToBeMoved.append(tracker[src].pop())
    else:
        cratesToBeMoved = tracker[src][len(tracker[src]) - numCratesToBeMoved :]
        del tracker[src][len(tracker[src]) - numCratesToBeMoved :]

    tracker.setdefault(dst, []).extend(cratesToBeMoved)


with open("5_in.txt") as file:
    for line1 in file:
        line = line1.rstrip()
        if cratePosRegex.match(line):
            stackCrates(line)
        elif crateMoveRegex.match(line):
            _, num, _, src, _, dst = line.split()
            moveCrates(int(src), int(dst), int(num))

topStacks = ""
for i in sorted(tracker.keys()):
    topStacks += tracker[i][-1]
print("The top stacks are", topStacks)

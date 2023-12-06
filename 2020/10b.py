#!/usr/bin/env python3
import pprint
pp = pprint.PrettyPrinter(indent=2, width=120)
def ParseInput(postProcess=lambda x:x):
    global Input, InputFromFile
    lines = []

    if InputFromFile:
        fin = open(Input)
        lines = [ line.strip('\n') for line in fin.readlines() ]
        fin.close()
    else:
        lines = Input.strip('\n').split('\n')

    return list(map(postProcess, lines))
Lines = ParseInput(lambda x: int(x))
Lines.sort()
Lines.insert(0, 0)

# Store no. of arrangements for visited elements to reduce recursion
NumArrangementsFor={}

def CountArrangements(initList=[Lines[0]]):
    global Lines, NumArrangementsFor

    if initList[-1] == Lines[-1]:
        return 1

    totArrangements = 0
    initLastIdx = Lines.index(initList[-1])
    chkList = Lines[initLastIdx + 1:]

    for chkNum in chkList:
        if chkNum - initList[-1] <= 3:
            if chkNum not in NumArrangementsFor:
                NumArrangementsFor[chkNum] = CountArrangements(initList + [chkNum])
            totArrangements += NumArrangementsFor[chkNum]
        else:
            break

    return totArrangements


totArrangements = CountArrangements()
print("Total no. of arrangements=", totArrangements, sep='')

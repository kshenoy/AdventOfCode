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

def ProcessInput():
    global Grid, LimX, LimY, LimZ, LimW

    lines = ParseInput()
    LimY = range(0, len(lines))
    LimX = range(0, len(lines[0]))
    LimZ = range(0, 1)
    LimW = range(0, 1)
    Grid = set()

    for y in LimY:
        for x in LimX:
            Grid.add((x,y,0,0)) if lines[y][x] == "#" else None
ProcessInput()

def PrintGrid():
    global Grid, LimX, LimY, LimZ, LimW

    # Now print it
    for w in LimW:
        for z in LimZ:
            print("w=", w, ", z=", z, sep='')
            for y in LimY:
                print("  ", end='')
                for x in LimX:
                    print("#" if (x,y,z,w) in Grid else ".", end="")
                print()
            print()

def GetNumActiveNeighbors(x, y, z, w):
    numActiveNeighbors = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                for l in range(w-1,w+2):
                    if (i,j,k,l) == (x,y,z,w):
                        continue
                    numActiveNeighbors += 1 if (i,j,k,l) in Grid else 0
    return numActiveNeighbors

def DoCycle(numIter=1):
    global Grid, LimX, LimY, LimZ, LimW

    for iter in range(numIter):
        # We need to look 1 unit farther in each direction and evaluate
        LimX=range(LimX.start - 1, LimX.stop + 1)
        LimY=range(LimY.start - 1, LimY.stop + 1)
        LimZ=range(LimZ.start - 1, LimZ.stop + 1)
        LimW=range(LimW.start - 1, LimW.stop + 1)

        newGrid = set()
        for w in LimW:
            for z in LimZ:
                for y in LimY:
                    for x in LimX:
                        getNumActiveNeighbors = GetNumActiveNeighbors(x, y, z, w)
                        # print((x,y,z), ": NumNeighbors=", getNumActiveNeighbors)
                        if (x,y,z,w) in Grid and (getNumActiveNeighbors in range(2,4)):
                            newGrid.add((x,y,z,w))
                        if (x,y,z,w) not in Grid and (getNumActiveNeighbors == 3):
                            newGrid.add((x,y,z,w))

        Grid = newGrid

DoCycle(6)
print("Num active cubes=", len(Grid), sep='')

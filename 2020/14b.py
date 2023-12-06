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
import re

Lines = ParseInput()
Mask0 = 0  # Set bits are 0
Mask1 = 0  # Set bits are 1
MaskX = 0  # Set bits are X
Mem={}

def ParseInstr(line):
    words = [ word.strip() for word in line.split('=') ]
    if words[0] == "mask":
        mask1, mask0, maskX = MakeMasks(words[1])
        return { "Cmd":"Mask", "Mask0":mask0, "Mask1":mask1, "MaskX":maskX }
    else:
        p = re.compile("^mem\[(?P<memLoc>\d+)]")
        m = p.search(words[0])
        memLoc = int(m['memLoc'])
        val = int(words[1])
        return { "Cmd":"Mem", "Loc":memLoc, "Val":val}

def MakeMasks(_mask):
    mask0 = int(_mask.replace('1', 'X').replace('0', '1').replace('X', '0'), base=2)
    mask1 = int(_mask.replace('X', '0'), base=2)
    maskX = int(_mask.replace('1', '0').replace('X', '1'), base=2)
    return (mask1, mask0, maskX)

FloatBits = []
for line in Lines:
    op = ParseInstr(line)
    if op['Cmd'] == "Mask":
        Mask0 = op['Mask0']
        Mask1 = op['Mask1']
        MaskX = op['MaskX']

        FloatLoc = []
        val = 1
        while val <= MaskX:
            if MaskX & val != 0:
                FloatLoc += [i + val for i in FloatLoc] if len(FloatLoc) != 0 else [0, val]
            val = val << 1

        print(line, ": Mask1=", Mask1, ", MaskX=", MaskX, ", FloatLoc=", FloatLoc, sep='') if Debug else None

    else:
        print(line) if Debug else None
        for loc in FloatLoc:
            memLoc = loc + ((op['Loc'] & ~MaskX) | Mask1)
            Mem[memLoc] = op['Val']

pp.pprint(Mem) if Debug else None
memSum = sum(Mem.values())
print("Sum of all elements in Memory=", memSum, sep='') if Verbose else None

Lines = [ line.strip('\n') for line in open("2_in.txt").readlines() ]

numValid = 0
for line in Lines:
    words = line.strip('\n').split(' ')
    validRange = [ int(i) for i in words[0].split('-') ]
    chkChar = words[1].strip(':')

    allMatchedChars = [ i for i in words[2] if (i == chkChar) ]
    if (len(allMatchedChars) >= validRange[0]) and (len(allMatchedChars) <= validRange[1]):
        numValid+=1

print(numValid)


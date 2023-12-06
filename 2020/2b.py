Lines = [ line.strip('\n') for line in open("2_in.txt").readlines() ]

numValid = 0
for line in Lines:
    words = line.strip('\n').split(' ')
    validPos = [ (int(i) - 1) for i in words[0].split('-') ]
    chkChar = words[1].strip(':')
    testStr = words[2]

    if ((testStr[validPos[0]] == chkChar) and (testStr[validPos[1]] != chkChar)) \
       or ((testStr[validPos[0]] != chkChar) and (testStr[validPos[1]] == chkChar)):
        numValid += 1

print(numValid)


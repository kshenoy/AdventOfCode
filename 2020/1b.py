Lines = [ int(i) for i in open("1_in.txt").readlines() ]

def GetSmallest(numList, n):
    smallestN = []
    for i in numList:
        smallestN.append(i)
        if len(smallestN) > n:
            smallestN.remove(max(smallestN))
    return smallestN

smallestN = GetSmallest(Lines, 2)
maxNum = 2020 - sum(smallestN)
numFilt = [ i for i in Lines if (i <= maxNum) ]

for i in range(len(numFilt) - 2):
    for j in range(i+1, len(numFilt) - 1):
        for k in range(j+1, len(numFilt)):
            if (numFilt[i] + numFilt[j] + numFilt[k] == 2020):
                prod = numFilt[i] * numFilt[j] * numFilt[k]
                print("Product of numbers is", prod)
                break


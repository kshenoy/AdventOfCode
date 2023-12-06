Lines = [ int(i) for i in open("1_in.txt").readlines() ]

numFilt = [ x for x in Lines if (x <= (2020 - min(Lines))) ]

for i in range(len(numFilt) - 1):
    for j in range(i+1, len(numFilt)):
        if (numFilt[i] + numFilt[j] == 2020):
            prod = numFilt[i] * numFilt[j]
            print("Product of numbers is", prod)
            break


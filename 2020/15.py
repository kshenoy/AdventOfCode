#!/usr/bin/env python3
import pprint
pp = pprint.PrettyPrinter(indent=2, width=120)

Num = [ int(i) for i in Input.strip('\n').split(',') ]
Ages = { i:[Num.index(i) + 1] for i in Num }
Last = Num[-1]
Turn = len(Num)

while Turn < Stop:
    Turn += 1
    Last = 0 if len(Ages[Last]) <= 1 else Ages[Last][-1] - Ages[Last][-2]

    Ages.setdefault(Last, [])
    Ages[Last].append(Turn)
    if len(Ages[Last]) > 2:
        Ages[Last].pop(0)

    print("Last=", Last, ", Ages=", Ages, sep='') if Debug else None

print(Stop, "th number spoken=", Last, sep='') if Verbose else print(Last)

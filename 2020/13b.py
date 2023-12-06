#!/usr/bin/env python3
import pprint
from functools import reduce
from operator import mul
from chinese_remainder_solver import ChineseRemainderSolver

pp = pprint.PrettyPrinter(indent=2, width=120)


# id_line = "7,13,x,x,59,x,31,19"
fin = open("13_in.txt")
id_line = fin.readlines()[1]

# The example problem can be expressed like this where we need to find t
# t =  7a - 0
# t = 13b - 1
# t = 59e - 4
# t = 31d - 6
# t = 19c - 7
#
# This can be written as and can be solved using the Chinese Remainder Theorem
# t ≡  0 (mod  7) ≡  0 (mod  7)
# t ≡ -1 (mod 13) ≡ 12 (mod 13)
# t ≡ -4 (mod 59) ≡ 55 (mod 59)
# t ≡ -6 (mod 31) ≡ 25 (mod 31)
# t ≡ -7 (mod 19) ≡ 12 (mod 19)

input = []
for i, id in enumerate(id_line.split(",")):
    if id != "x":
        input.append((-i % int(id), int(id)))

print(ChineseRemainderSolver(input).solve())

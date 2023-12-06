#!/usr/bin/env python3
import pprint
from functools import reduce
from operator import mul

pp = pprint


class ChineseRemainderSolver:
    def __init__(self, input, debug=False):
        # Input is expected as a list of pair (as a tuple) of ints with the numbers in the tuple representing the remainder and then the number
        self.N = []
        self.R = []
        self.P = []
        self.X = []
        self.M = 0
        self.Debug = debug

        for r, n in input:
            self.N.append(n)
            self.R.append(r)
        print("N=", pp.pformat(self.N), sep="") if self.Debug else None
        print("R=", pp.pformat(self.R), sep="") if self.Debug else None

    def solve(self) -> int:
        # According to the Chinese Remainder Theorem, we start by computing the products
        self.compute_products()

        # Now we invert these using p * x ≡  r (mod n)
        self.compute_inverted_products()

        return self.compute_final_solution()

    def compute_products(self):
        self.M = reduce(mul, self.N, 1)
        print("M=", self.M, sep="") if self.Debug else None

        self.P = [int(self.M / n) for n in self.N]
        print("P=", pp.pformat(self.P), sep="") if self.Debug else None

    def compute_inverted_products(self):
        for n, p in zip(self.N, self.P):
            p = p % n
            i = 1
            while True:
                if p * i % n == 1:
                    self.X.append(i)
                    break
                i += 1
        print("X=", pp.pformat(self.X), sep="") if self.Debug else None

    def compute_final_solution(self):
        return sum([p * r * x for p, r, x in zip(self.P, self.R, self.X)]) % self.M

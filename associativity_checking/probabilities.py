# Calculates the average error of the randomized checking, when we repeat
# the algorithm t number of times. We try it for t = 1, 2, ..., 10.

# Usage: receives as argument the number m of times we test the algorithm
# for each t. In the standard input, we receive n and A, the Cayley Table
# of an operation on a n-element set. The operation must be
# non-associative.

import numpy as np
import sys
from associativity_checker import *

def main(argv):
    m = int(argv[1])
    n = int(input())
    A = np.empty([n,n])
    
    for i in range(n):
        input_line = [int(x) for x in input().split()]
        for j in range(n):
            A[i,j] = input_line[j]

    checker = AssociativityChecker(A, n)
    print("Number of randomized checkings | Frequency of wrong answers")
    print("--- | ---")
    for t in range(1,11):
        ctr = 0
        for _ in range(m):
            ctr += 1 if checker.is_associative_random(t) else 0
        print("t = ", t, " | ",  ctr/m)

if __name__ == '__main__':
    np.set_printoptions(precision=5)
    main(sys.argv)

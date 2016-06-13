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

    print("Probability of failure, testing", m, "times each:")
    for t in range(1,11):
        ctr = 0
        for _ in range(m):
            ctr += 1 if checker.is_associative_random(t) else 0
        print("t = ", t, " | ",  ctr/m)

if __name__ == '__main__':
    np.set_printoptions(precision=5)
    main(sys.argv)
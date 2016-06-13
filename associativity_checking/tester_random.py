import numpy as np
import sys
from associativity_checker import *

def main(argv):
    t = int(argv[1])
    n = int(input())
    A = np.empty([n,n], dtype=np.int)
    
    for i in range(n):
        input_line = [int(x) for x in input().split()]
        for j in range(n):
            A[i,j] = input_line[j]

    checker = AssociativityChecker(A, n)
    print("Is it associative?", checker.is_associative_random(t))

if __name__ == '__main__':
    np.set_printoptions(precision=5)
    main(sys.argv)

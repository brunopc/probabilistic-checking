# Tests the algorithm for checking associativity in the cancellative case.
# Note that it also works when it is not cancellative, but we cannot
# guarantee a O(n^2*lgn) complexity.
# No randomization involved.

# Usage: In the standard input, we receive n and A, the Cayley Table
# of an operation on a n-element set.

import numpy as np
import sys
from associativity_checker import *

def main(argv):
    n = int(input())
    A = np.empty([n,n], dtype=np.int)
    
    for i in range(n):
        input_line = [int(x) for x in input().split()]
        for j in range(n):
            A[i,j] = input_line[j]

    checker = AssociativityChecker(A, n)
    cancellative = checker.is_cancellative()
    print("Is it cancellative?", cancellative)
    associative = checker.is_associative_deterministic()
    print("Is it associative?", associative)
    print("Is it a group?", cancellative and associative)

if __name__ == '__main__':
    np.set_printoptions(precision=5)
    main(sys.argv)


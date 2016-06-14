# Prints the Cayley Table of a non-associative operation of size n.
# The result is intended to be piped to the checkers as a test-case.
# Usage: python3 non_associative.py n

import numpy as np
import sys

def main(argv):
    n = int(argv[1])
    A = np.zeros([n,n], dtype=np.int)
    A[n-2,n-1] = n-2
    print(n)
    for i in range(n):
        for j in range(n):
            print(A[i,j], end=" ")
        print("")

if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main(sys.argv)

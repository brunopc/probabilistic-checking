# Usage: python3 wizard.py n t d
# where n: dimension of the matrix
#       t: number of randomized tests
#       d: density of error

import numpy as np
import sys

def test_equality(A, B, C, n, t):
    isEqual = True
    for _ in range(t):
        x = np.random.binomial(1, 0.5, n)
        Cx = np.dot(C,x)
        ABx = np.dot(A, np.dot(B,x))
        if ( not (np.allclose(Cx, ABx)) ):
            isEqual = False
    return isEqual

def main (argv):
    n, t, d = int(argv[1]), int(argv[2]), float(argv[3])

    A = np.random.rand(n,n)
    B = np.random.rand(n,n)
    C = np.dot(A,B)

    S = np.random.binomial(1, d, [n,n])*np.random.normal(0, 1, [n,n])
    E = C + S

    C_isEqual = test_equality(A, B, C, n, t)
    E_isEqual = test_equality(A, B, E, n, t)

    print (C_isEqual, E_isEqual)

if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main(sys.argv)

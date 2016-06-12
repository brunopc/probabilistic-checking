# Usage: python3 wizard.py n m t d
# where n: dimension of the matrix
#       m: number of test cases
#       t: number of randomized checkings
#       d: density of error of the wrong matrix

import numpy as np
import sys

# Tests if C = AB using Freivalds Algorithm
def test_equality(A, B, C, n, t):
    isEqual = True
    for _ in range(t):
        if (not isEqual):
            break
        x = np.random.binomial(1, 0.5, n)
        Cx = np.dot(C,x)
        ABx = np.dot(A, np.dot(B,x))
        if ( not (np.allclose(Cx, ABx)) ):
            isEqual = False
    return isEqual

def main (argv):
    n, m, t, d = int(argv[1]), int(argv[2]), int(argv[3]), float(argv[4])

    c_ctr = e_ctr = 0
    for i in range(m):
        A = np.random.rand(n,n)
        B = np.random.rand(n,n)
        C = np.dot(A,B) 
        # C = AB

        # S: error matrix
        S = np.random.binomial(1, d, [n,n])*np.random.normal(0, 1, [n,n])
        E = C + S 
        # E = AB + S, where S is an error matrix

        # S_not_zero: checks if S is not zero 
        S_not_zero = np.any(S)
        C_isEqual = test_equality(A, B, C, n, t)
        E_isEqual = test_equality(A, B, E, n, t)

        c_ctr += 1 if C_isEqual else 0
        e_value = 0 if E_isEqual else 1
        
        # E = AB when S = 0, so we check this case
        e_ctr += e_value if S_not_zero else 1-e_value

    print ("Proportion of correct results:")
    print ("Correct matrix: ", c_ctr/m)
    print ("Wrong matrix: ", e_ctr/m)

if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main(sys.argv)

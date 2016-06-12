# Usage:
# Receives a table of n numbers. Each entry is a number between 0 and n-1.

import numpy as np
import sys

S_SIZE = 7

class AssociativityTester:
    def __init__(self, A, n):
        self.A = A
        self.n = n

    def op(s, u, v):
        w = np.zeros(s.n, dtype=np.int)
        for x in range(s.n):
            for y in range(x, s.n):
                exy = s.A[x, y]
                w[exy] += u[x]*v[y]
                w[exy] %= S_SIZE
        return w

    def is_associative(s):
        u = np.random.randint(1, S_SIZE+1, size=s.n)
        v = np.random.randint(1, S_SIZE+1, size=s.n)
        w = np.random.randint(1, S_SIZE+1, size=s.n)
        return (s.op(s.op(u,v), w) == s.op(u, s.op(v,w))).all()

def main(argv):
    n = int(input())
    A = np.empty([n,n])
    
    for i in range(n):
        input_line = [int(x) for x in input().split()]
        for j in range(n):
            A[i,j] = input_line[j]

    tester = AssociativityTester(A, n)

    print(tester.is_associative())

if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main(sys.argv)

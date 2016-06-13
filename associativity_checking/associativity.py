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
            for y in range(s.n):
                exy = s.A[x, y]
                w[exy] += u[x]*v[y]
                w[exy] %= S_SIZE
        return w

    def is_associative(s):
        # random vectors with entries in the finite field Z/Z_{S_SIZE}
        u = np.random.randint(1, S_SIZE+1, size=s.n)
        v = np.random.randint(1, S_SIZE+1, size=s.n)
        w = np.random.randint(1, S_SIZE+1, size=s.n)
        return (s.op(s.op(u,v), w) == s.op(u, s.op(v,w))).all()

    def is_associative_times(s,t):
        for _ in range(t):
            if (not s.is_associative()): return False
        return True


def main(argv):
    m, t = int(argv[1]), int(argv[2])
    n = int(input())
    A = np.empty([n,n])
    
    for i in range(n):
        input_line = [int(x) for x in input().split()]
        for j in range(n):
            A[i,j] = input_line[j]

    tester = AssociativityTester(A, n)
    ctr = 0
    for _ in range(m):
        ctr += 1 if tester.is_associative_times(t) else 0
    print(ctr/m)

if __name__ == '__main__':
    np.set_printoptions(precision=5)
    main(sys.argv)

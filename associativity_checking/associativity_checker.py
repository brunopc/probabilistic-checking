import numpy as np
import sys
from collections import deque

S_SIZE = 7

class AssociativityChecker:
    def __init__(self, A, n):
        # A is the Cayley Table of an operation on a n-element set.
        # A must be a n*n matrix, each entry a number between 0 and n-1.
        self.A = A
        self.n = n

    # Linear extension of the operation
    def op(s, u, v):
        w = np.zeros(s.n, dtype=np.int)
        for x in range(s.n):
            for y in range(s.n):
                exy = s.A[x,y]
                w[exy] += u[x]*v[y]
                w[exy] %= S_SIZE
        return w

    # Checks if the operation is associative using the algorithm of
    # Rajagopalan and Schulman.
    def is_associative_random(s,t):
        for _ in range(t):
            # random vectors with entries in the finite field Z/Z_{S_SIZE}*
            u = np.random.randint(1, S_SIZE+1, size=s.n)
            v = np.random.randint(1, S_SIZE+1, size=s.n)
            w = np.random.randint(1, S_SIZE+1, size=s.n)
            is_it = (s.op(s.op(u,v), w) == s.op(u, s.op(v,w))).all()
            if (not is_it): return False
        return True

    # Returns True if the operation is cancellative.
    # We just check the definition.
    def is_cancellative(s):
        for x in range(s.n):
            xs = np.zeros(s.n, dtype=bool)
            for y in range(s.n):
                xs[s.A[x,y]] = True
            if (not xs.all()): return False
        return True

    # Returns a set of generators of the operation. In particular, the set
    # has size at most lgn + 1 when the operation is cancellative.
    def generators(s):
        # set of generators
        gen = []
        # inlist: elements in the set generated by gen
        inlist = []
        is_inlist = np.zeros(s.n, dtype=bool)
        # outlist: elements out of the set generated by gen
        # here we use deque as a linked list
        outlist = deque(range(0,s.n))

        # we just insert elements to gen until it generates the whole set
        while len(outlist) != 0:
            x = outlist.popleft()
            while is_inlist[x] and len(outlist):
                x = outlist.popleft()
            if (is_inlist[x]): break
            gen.append(x)

            new_elements = deque([x])
            while (len(new_elements) != 0):
                x = new_elements.popleft()
                if (is_inlist[x]): continue
                inlist.append(x)
                is_inlist[x] = True
                for y in inlist:
                    if (not is_inlist[s.A[x,y]]):
                        new_elements.append(s.A[x,y])
                    if (not is_inlist[s.A[y,x]]):
                        new_elements.append(s.A[y,x])
        return gen

    # True if the operation is associative.
    def is_associative_deterministic(s):
        gs = s.generators()
        for x in range(s.n):
            for y in range(s.n):
                for g in gs:
                    if (s.A[s.A[x,g],y] != s.A[x,s.A[g,y]]):
                        return False
        return True

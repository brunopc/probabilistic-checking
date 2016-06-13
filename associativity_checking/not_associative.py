import numpy as np
import sys

def main(argv):
    n = int(argv[1])
    A = np.zeros([n,n], dtype=np.int)
    A[1,2] = 1
    print(n)
    for i in range(n):
        for j in range(n):
            print(A[i,j], end=" ")
        print("")

if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main(sys.argv)

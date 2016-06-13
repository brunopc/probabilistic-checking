import sys

def main(argv):
    n = int(argv[1])
    print(n)
    for i in range(n):
        for j in range(n):
            print((i+j)%n, end=" ")
        print("")

if __name__ == '__main__':
    main(sys.argv)

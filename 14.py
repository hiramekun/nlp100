import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    with open('hightemp.txt') as f:
        for i in range(n):
            print(f.readline().strip('\n'))

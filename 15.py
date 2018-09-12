import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    with open('hightemp.txt') as f:
        lines = f.readlines()
        for i in reversed(range(n)):
            print(lines[-(i + 1)].strip('\n'))

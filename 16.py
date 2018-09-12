import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    with open('hightemp.txt') as f:
        lines = f.readlines()
        ave = int(len(lines) / n)
        for i in range(n):
            print('Next file...')
            for j in range(ave * i, ave * (i + 1)):
                print(lines[j])

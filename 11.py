if __name__ == '__main__':
    with open('hightemp.txt') as f:
        for l in f:
            print(l.replace('\t', ' ').strip('\n'))

if __name__ == '__main__':
    with open('col1.txt') as f:
        print(set([l.strip('\n') for l in f.readlines()]))

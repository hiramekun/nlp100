if __name__ == '__main__':
    with open('british.txt') as f:
        for l in f:
            if l.startswith('[[Category'):
                print(l)

if __name__ == '__main__':
    f1 = open('col1.txt')
    f2 = open('col2.txt')
    with open('combine.txt', 'w') as f:
        for l1, l2 in zip(f1, f2):
            f.write(l1.strip('\n') + l2)

    f1.close()
    f2.close()

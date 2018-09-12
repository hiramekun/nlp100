if __name__ == '__main__':
    f1 = open('col1.txt', 'w')
    f2 = open('col2.txt', 'w')
    with open('hightemp.txt') as f:
        for l in f:
            f1.write(l[0] + '\n')
            f2.write(l[1] + '\n')
    f1.close()
    f2.close()

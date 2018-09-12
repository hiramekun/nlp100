if __name__ == '__main__':
    with open('hightemp.txt') as f:
        print("".join(sorted(f.readlines(), key=lambda x: x.split('\t')[2], reverse=True)))

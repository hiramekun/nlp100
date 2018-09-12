if __name__ == '__main__':
    with open('hightemp.txt') as f:
        lines = f.readlines()
        print("".join(
            sorted(lines, key=lambda x: (''.join([l[0] for l in lines]).count(x[0]), x),
                   reverse=True)))

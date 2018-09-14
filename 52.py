import re

from stemming import porter


def get_sentence():
    reg = re.compile(r'(.*?[.;:?!])\s([A-Z].*?\.)')
    with open('nlp.txt') as f:
        for l in f:
            l = l.strip()
            match = reg.split(l)
            if len(match) > 0:
                for line in match:
                    if len(line) > 0:
                        yield (line.strip())


if __name__ == '__main__':
    for line in get_sentence():
        print(''.join([porter.stem(word.strip(',.')) + '\n' for word in line.split(' ')]))

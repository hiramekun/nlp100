import re

if __name__ == '__main__':
    reg = re.compile(r'(.*?[.;:?!])\s([A-Z].*?\.)')
    with open('nlp.txt') as f:
        for l in f:
            l = l.strip()
            match = reg.split(l)
            if len(match) > 0:
                for line in match:
                    if len(line) > 0:
                        print(line.strip())

import re

if __name__ == '__main__':
    reg = re.compile(r'^(={2,})\s*(.+?)\s*\1.*$')
    result = []
    with open('british.txt') as f:
        for l in f:
            res = reg.findall(l)
            if len(res) != 0:
                result.append(res)
    for l in result:
        level = len(l[0][0]) - 1
        print(
            '{indent}{sect}({level})'.format(indent='\t' * (level - 1), sect=l[0][1], level=level))

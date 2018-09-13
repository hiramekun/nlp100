import re

if __name__ == '__main__':
    reg = re.compile(r'(?:File|ファイル):(.*?)\|')
    with open('british.txt') as f:
        for l in f:
            result = reg.findall(l)
            if len(result) != 0:
                print(result[0])

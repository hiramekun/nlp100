import json

if __name__ == '__main__':
    with open('jawiki-country.json') as f:
        lines = f.readlines()

    with open('british.txt', 'w') as rf:
        for l in lines:
            jdic = json.loads(l)
            if jdic['title'] == 'イギリス':
                rf.write(jdic['text'])

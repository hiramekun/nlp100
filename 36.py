from collections import Counter

import MeCab

fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'


def parse_neko():
    with open(fname) as data_file, open(fname_parsed, 'w') as out_file:
        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neco_lines():
    with open(fname_parsed) as file_parsed:
        morphemes = []
        for line in file_parsed:
            cols = line.split('\t')
            if len(cols) < 2:
                continue
            res_cols = cols[1].split(',')
            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []


if __name__ == '__main__':
    parse_neko()
    word_counter = Counter()
    for line in neco_lines():
        word_counter.update([morpheme['surface'] for morpheme in line])

    list_word = word_counter.most_common()
    print(list_word)

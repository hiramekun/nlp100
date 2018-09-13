import os
import random

if __name__ == '__main__':
    data_dir = 'rt-polaritydata/rt-polaritydata'
    path_neg = os.path.join(data_dir, 'rt-polarity-utf8.neg')
    path_pos = os.path.join(data_dir, 'rt-polarity-utf8.pos')

    with open('sentiment.txt', 'w') as f_write, open(path_neg) as f_neg, open(path_pos) as f_pos:
        sentences = []
        sentences.extend(['-1 ' + l_neg for l_neg in f_neg])
        sentences.extend(['+1 ' + l_pos for l_pos in f_pos])
        random.shuffle(sentences)
        f_write.write(''.join([line for line in sentences]))

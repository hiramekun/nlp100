import numpy as np
from stemming import porter

stop_words = (
    'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,'
    'as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,'
    'either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,'
    'him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,'
    'likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,'
    'on,only,or,other,our,own,rather,said,say,says,she,should,since,so,'
    'some,than,that,the,their,them,then,there,these,they,this,tis,to,too,'
    'twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,'
    'will,with,would,yet,you,your').lower().split(',')


def is_stop_word(string):
    return string.lower() in stop_words


def hypothesis(data_x, theta):
    return 1.0 / (1.0 + np.exp(-data_x.dot(theta)))


def extract_features(data, dict_features):
    data_one_x = np.zeros(len(dict_features) + 1, dtype=np.float64)
    data_one_x[0] = 1
    for word in data.split(' '):
        word = word.strip()
        if is_stop_word(word):
            continue

        word = porter.stem(word)
        try:
            data_one_x[dict_features[word]] = 1
        except:
            pass
    return data_one_x


def load_dict_features():
    with open('features.txt') as f:
        return {line.strip(): i for i, line in enumerate(f, start=1)}


if __name__ == '__main__':
    dict_features = load_dict_features()
    theta = np.load('theta.npy')
    review = input('レビューを入力してください--> ')
    data_one_x = extract_features(review, dict_features)
    h = hypothesis(data_one_x, theta)
    if h > 0.5:
        print(f'label:+1 ({h})')
    else:
        print(f'label:-1 ({1-h})')

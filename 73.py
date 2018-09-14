import numpy as np
from stemming import porter

alpha = 10
epoch = 3000
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


def cost(data_x, theta, data_y):
    m = data_y.size
    h = hypothesis(data_x, theta)
    j = 1 / m * np.sum(-data_y * np.log(h) - (np.ones(m) - data_y) * np.log(np.ones(m) - h))
    return j


def gradient(data_x, theta, data_y):
    m = data_y.size
    h = hypothesis(data_x, theta)
    grad = 1 / m * (h - data_y).dot(data_x)
    return grad


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


def create_training_set(sentiments, dict_features):
    data_x = np.zeros([len(sentiments), len(dict_features) + 1], dtype=np.float64)
    data_y = np.zeros(len(sentiments), dtype=np.float64)

    for i, line in enumerate(sentiments):
        data_x[i] = extract_features(line[3:], dict_features)
        if line[0:2] == '+1':
            data_y[i] = 1

    return data_x, data_y


def train(data_x, data_y, alpha, epoch):
    theta = np.zeros(data_x.shape[1])
    c = cost(data_x, theta, data_y)
    print(f'\t学習開始\tcost:{c}')

    grad = 0.0
    for i in range(1, epoch + 1):
        grad = gradient(data_x, theta, data_y)
        theta -= alpha * grad
        if i % 100 == 0:
            c = cost(data_x, theta, data_y)
            e = np.max(np.abs(alpha * grad))
            print(f'\t学習中({i})\tcost:{c}\tE:{e}')

    c = cost(data_x, theta, data_y)
    e = np.max(np.abs(alpha * grad))
    print(f'\t学習完了({i})\tcost:{c}\tE:{e}')
    return theta


if __name__ == '__main__':
    dict_features = load_dict_features()
    with open('sentiment.txt') as f:
        data_x, data_y = create_training_set(list(f), dict_features)

    print(f'学習率:{alpha}\tepoch:{epoch}')
    theta = train(data_x, data_y, alpha=alpha, epoch=epoch)
    np.save('theta.npy', theta)

from collections import Counter

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


def is_stopword(string):
    return string.lower() in stop_words


if __name__ == '__main__':
    word_counter = Counter()
    with open('sentiment.txt') as f:
        for line in f:
            for word in line[3:].split(' '):
                word = word.strip()
                if is_stopword(word):
                    continue
                word = porter.stem(word)
                if word != '!' and word != '?' and len(word) <= 1:
                    continue

                word_counter.update([word])

    features = [word for word, count in word_counter.items() if count >= 6]
    with open('features.txt', 'w') as f:
        print(*features, sep='\n', file=f)

def generate_word_ngram(sequence, n=2):
    s1 = sequence.split(' ')
    ans = [s1[i:i + n] for i in range(len(s1) - n + 1)]
    return ans


def generate_char_ngram(sequence, n=2):
    s1 = ''.join(sequence.split(' '))
    ans = [s1[i:i + n] for i in range(len(s1) - n + 1)]
    return ans


if __name__ == '__main__':
    print(generate_word_ngram('I am an NLPer'))
    print(generate_char_ngram('I am an NLPer', 3))

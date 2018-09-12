import random


def shuffle_word(word):
    shuffled = list(word[1:-1])
    random.shuffle(shuffled)
    return word[0] + ''.join(shuffled) + word[-1]


if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
    print(' '.join([shuffle_word(s) if len(s) > 4 else s for s in sentence.split(' ')]))

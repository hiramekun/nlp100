def generate_char_ngram(sequence, n=2):
    s1 = ''.join(sequence.split(' '))
    ans = [s1[i:i + n] for i in range(len(s1) - n + 1)]
    return ans


if __name__ == '__main__':
    s1 = 'paraparaparadise'
    s2 = 'paragraph'
    X = set(generate_char_ngram(s1))
    Y = set(generate_char_ngram(s2))
    print(f'X: {X}')
    print(f'Y: {Y}')
    print(f'和集合: {X | Y}')
    print(f'積集合: {X & Y}')
    print(f'差集合: {X - Y}')
    print(f'seがXに入るか: {"se" in X}')
    print(f'seがYに入るか: {"se" in Y}')

def cipher(sentence):
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in sentence)


if __name__ == '__main__':
    print(cipher("Hello, world!"))

def generate_sentence(x, y, z):
    return f'{x}時の{y}は{z}'


if __name__ == '__main__':
    print(generate_sentence(12, '気温', '22.4'))

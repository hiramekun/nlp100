if __name__ == '__main__':
    s1 = 'Now I need a drink, alcohilic of course, after the heavy lectures involving quantum mechanics.'
    s1.replace(',', '').replace('.', '')
    ans = [len(w) for w in s1.split(' ')]
    print(ans)

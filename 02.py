if __name__ == '__main__':
    str1 = 'パトカー'
    str2 = 'タクシー'
    ans = [s1 + s2 for s1, s2 in zip(str1, str2)]
    print("".join(a for a in ans))

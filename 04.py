if __name__ == '__main__':
    s1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    s1.replace('.', '')
    dic = {}
    for i, s in enumerate(s1.split(' ')):
        if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            dic[i + 1] = s[0]
        else:
            dic[i + 1] = s[:2]
    print(dic)

import random

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
    s_list = sentence.split(' ')
    idx_lessword = [i for i, s in enumerate(s_list) if len(s) > 4]
    shuffled = [s for i, s in enumerate(s_list) if i not in idx_lessword]
    random.shuffle(shuffled)
    ans = []
    j = 0
    for i in range(len(s_list)):
        if i in idx_lessword:
            ans.append(s_list[i])
        else:
            ans.append(shuffled[j])
            j += 1

    print(' '.join(ans))

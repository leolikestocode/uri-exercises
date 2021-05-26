n = []

while 1:
    try:
        n.append(input())

    except:
        n = ' '.join(n).strip()
        s = 0
        n_words = n.split(' ')
        for i in range(0, len(n_words)):

            if (s + len(n_words[i]) > 80):
                print('')
                s = 0

            if (n_words[i] == "<br>"):
                print('')
                s = 0
                continue
            elif (n_words[i] == "<hr>"):
                if (s != 0):
                    print('')
                print('-' * 80)
                s = 0
                continue

            if (n_words[i] != ' '):
                print(n_words[i], end='')
                s += len(n_words[i]) + 1

            if (i + 1 < len(n_words) and s + len(n_words[i + 1]) <= 80 and n_words[i + 1] != '<hr>' and n_words[i + 1] != '<br>'):
                print(' ', end='')

        print('')
        break

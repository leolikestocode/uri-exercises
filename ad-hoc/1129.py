while 1:
    K = int(input())
    if K == 0:
        break

    for i in range(K):
        valores = input()
        num = valores.split(' ')
        item = ''

        for x in range(0, 5):
            if (int(num[x]) <= 127):
                if (x == 0):
                    item += 'A'
                if (x == 1):
                    item += 'B'
                if (x == 2):
                    item += 'C'
                if (x == 3):
                    item += 'D'
                if (x == 4):
                    item += 'E'

        if (len(item) == 1):
            print(item)
        else:
            print('*')

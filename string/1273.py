times = 0
while 1:
    n = int(input())
    if (n == 0):
        break

    if (times != 0):
        print('')

    times += 1

    arr = []
    maximo = 0

    for i in range(n):
        m = input()
        m_no_space = " ".join(m.split())

        if (len(m_no_space) > maximo):
            maximo = len(m_no_space)

        arr.append(m_no_space)

    space = ' '

    for item in arr:
        print('%s%s' % (space * (maximo - len(item)), item))

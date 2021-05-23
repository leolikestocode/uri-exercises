while 1:
    t = int(input())

    if (t == 0):
        break

    pessoas = []

    while t:
        t -= 1
        n = int(input())
        if n % 2 == 0:
            pessoas.append((2 * n) - 2)
        else:
            pessoas.append((2 * n) - 1)
    for i in pessoas:
        print(i)

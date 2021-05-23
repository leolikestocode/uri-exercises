while 1:
    n, m = map(int, input().split())

    if (n == 0 and m == 0):
        break

    notas = [2, 5, 10, 20, 50, 100]

    diff = m - n
    possible = False

    for i in range(len(notas)):
        if (possible):
            break
        for j in range(1, len(notas)):
            if (notas[j] + notas[i] == diff):
                possible = True
                break

    print('possible' if possible else 'impossible')

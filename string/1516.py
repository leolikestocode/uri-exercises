while 1:
    n, m = map(int, input().split())

    if (n == 0 and m == 0):
        break

    matriz = []

    for i in range(n):
        matriz.append(list(input()))

    a, b = map(int, input().split())

    new_n = int(a / n)
    new_m = int(b / m)

    for i in range(n):
        aux = ''
        for j in range(m):
            aux += new_m * matriz[i][j]

        for k in range(new_n):
            print(aux)

    print('')

while 1:
    n = int(input())

    if (n == 0):
        break

    gasto = []
    for i in range(n):
        gasto.append(float(input()))

    media = sum(gasto) / n
    filter_less = list(filter(lambda x: x < media, gasto))
    filter_less_length = len(filter_less)

    res = int((filter_less_length * media - sum(filter_less)) * 100)

    print('${:.2f}'.format(float(res / 100)))

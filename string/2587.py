n = int(input())
for i in range(n):
    a = list(input())
    b = list(input())
    c = list(input())

    indices = []

    for i in range(len(c)):

        if c[i] == '_':
            indices.append(i)

        if (len(indices) == 2):
            break

    if (a[indices[0]] == b[indices[1]] or a[indices[1]] == b[indices[0]]):
        print('Y')
    else:
        print('N')

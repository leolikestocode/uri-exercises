n = int(input())
h = list(map(int, input().split()))

mudancas = 0
padrao = 0
if h[0] == h[1]:
    print(0)
else:
    sobe = True if h[0] < h[1] else False

    for i in range(1, n - 1):
        if (h[i] == h[i + 1]):
            break
        if (h[i] < h[i + 1]):
            if (sobe):
                break
            else:
                sobe = True
        if (h[i] > h[i + 1]):
            if (not(sobe)):
                break
            else:
                sobe = False

        mudancas += 1

    print(1 if (mudancas + 2) == n else 0)

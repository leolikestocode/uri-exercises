while 1:
    arr = input().split()
    if (arr[0] == "0"):
        break

    a, b, c = arr

    a = int(a)
    b = int(b)
    c = int(c)

    print(int(((a * b * 100) / c) ** 0.5))

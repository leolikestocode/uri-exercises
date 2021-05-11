n = int(input())

for i in range(n):
    x, y = input().split()

    longest = len(x) if len(x) > len(y) else len(y)
    s = ''

    for j in range(longest):
        if (len(x) >= j + 1):
            s += x[j]
        if (len(y) >= j + 1):
            s += y[j]

    print(s)

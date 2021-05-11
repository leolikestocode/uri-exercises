n = int(input())

for i in range(n):
    t = list(input().lower())
    s = 1

    for j in range(len(t)):
        if ('aeios'.find(t[j]) != -1):
            s *= 3
        else:
            s *= 2

    print(s)

n = int(input())

for i in range(n):
    m = int(input())
    s = 0

    for j in range(m):
        item = list(input())

        for k in range(len(item)):
            s += ord(item[k]) - 65 + j + k

    print(s)

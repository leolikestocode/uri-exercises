while 1:
    try:
        n, m = input().split()
        n = int(n)
        m = int(m)
        s = 0
        for i in range(n, m + 1):
            if (len(set(str(i))) == len(str(i))):
                s += 1

        print(s)

    except EOFError:
        break

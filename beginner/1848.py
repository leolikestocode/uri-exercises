while 1:
    try:
        s = 0
        while 1:
            n = input()
            if (n == "caw caw"):
                break

            a = list(n)

            if (a[0] == "*"):
                s += 4
            if (a[1] == "*"):
                s += 2
            if (a[2] == "*"):
                s += 1

        print(s)
    except:
        break

while 1:
    try:
        h, m = input().split(':')

        if (h == "6" or h == "5"):
            print("Atraso maximo: 0")
        else:
            print("Atraso maximo:", (int(h) + 1 - 8) * 60 + int(m))
    except:
        break

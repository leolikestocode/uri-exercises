n = int(input())

for i in range(n):
    h, m, o = input().split()

    h = "0" + h if len(h) == 1 else h
    m = "0" + m if len(m) == 1 else m

    print("{}:{} - A porta {}!".format(h, m, "abriu" if o == "1" else "fechou"))
n = input()

while 1:
    h1, m1, h2, m2 = n.split()
    if (h1 == "0" and m1 == "0" and h2 == "0" and m2 == "0"):
        break

    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    init = h1 * 60 + m1
    final = (h2 + 24) * 60 + m2 if h2 < h1 or (h2 ==
                                               h1 and m2 < m1) else h2 * 60 + m2

    print(final - init)
    n = input()

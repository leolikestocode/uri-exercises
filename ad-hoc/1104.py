while 1:
    c1, c2 = input().split()
    if (c1 == "0" and c2 == "0"):
        break
    v1 = input().split(' ')
    v2 = input().split(' ')

    l = len(list(set(v1) - set(v2)))
    l2 = len(list(set(v2) - set(v1)))

    print(l if l < l2 else l2)

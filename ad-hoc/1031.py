def crise_energy(n, k):
    p = 0
    v = [x for x in range(1, int(n)+1)]

    while(len(v) > 1):
        v.pop(p)
        p = (p - 1 + k) % len(v)

        if (not(13 in v)):
            v = [0]

    return v[0] == 13


while 1:
    n = int(input())
    if n == 0:
        break
    r = 1
    while (not(crise_energy(n, r))):
        r += 1

    print(r)

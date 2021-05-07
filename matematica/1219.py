pi = 3.1415926535897
while 1:
    try:
        a, b, c = map(int, input().split())
        r_sunf = ((a * b * c) / (((a + b + c) * (b + c - a)
                  * (c + a - b) * (a + b - c)) ** 0.5))
        sunf = pi * r_sunf * r_sunf

        p_tri = (a + b + c) / 2
        a_tri = (p_tri * (p_tri - a) * (p_tri - b) * (p_tri - c)) ** 0.5

        r_rosas = a_tri / p_tri
        a_rosas = pi * r_rosas * r_rosas

        a_sunf = sunf - a_tri
        a_tri = a_tri - a_rosas

        print("{:.4f} {:.4f} {:.4f}".format(a_sunf, a_tri, a_rosas))

    except:
        break

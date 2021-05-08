pi = 3.14

while 1:
    try:
        v = float(input())
        d = float(input())

        print('ALTURA = {:.2f}'.format(v / (pi * (d / 2) ** 2)))
        print('AREA = {:.2f}'.format(pi * (d / 2) ** 2))
    except:
        break

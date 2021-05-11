import math

while 1:
    try:
        n = float(input())
        m = float(input())

        print(math.ceil(n) if n - int(n) - m > 0 else math.floor(n))

    except:
        break

import math

g = 9.80665
pi = 3.14159


def senoDe(a):
    return math.sin((a * pi) / 180)


def cossenoDe(a):
    return math.cos((a * pi) / 180)


h = float(input())
p1, p2 = map(int, input().split())
n = int(input())
for i in range(n):
    a, v = map(float, input().split())

    altura = ((v * senoDe(a)) * (v * senoDe(a))) / (2 * g)
    h_final = h + altura
    v0y = v * senoDe(a)
    v0x = v * cossenoDe(a)
    alcance = ((v0x * v0y) / g) + (v0x * (((2 * h_final) / g) ** 0.5))

    if (not(alcance >= p1 and alcance <= p2)):
        print("{:.5f} -> NUCK".format(alcance))
    else:
        print("{:.5f} -> DUCK".format(alcance))

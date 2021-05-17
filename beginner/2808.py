# 97 and 104 are the ascii number to a and h

x1, x2 = input().split()
x1 = list(x1)
x2 = list(x2)

mascara = [
    [-2, +1],
    [-2, -1],
    [+2, +1],
    [+2, -1],
    [-1, +2],
    [+1, +2],
    [-1, -2],
    [+1, -2],
]

for i in mascara:
    if ((ord(x1[0]) + i[0]) == ord(x2[0]) and (ord(x1[1]) + i[1]) == ord(x2[1])):
        print('VALIDO')
        break
else:
    print('INVALIDO')

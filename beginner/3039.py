n = int(input())
c = 0
b = 0

for i in range(n):
    x, y = input().split()
    if (y == "F"):
        b += 1
    if (y == "M"):
        c += 1

print(c, "carrinhos")
print(b, "bonecas")

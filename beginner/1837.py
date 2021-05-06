a, b = input().split()

a = int(a)
b = int(b)

print(int(a / b), a % (b if b > 0 else b * -1))

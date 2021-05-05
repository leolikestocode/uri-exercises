m = int(input())
f1 = int(input())
f2 = int(input())
f3 = m - f1 - f2

print(f1 if f1 > f2 and f1 > f3 else f2 if f2 > f3 else f3)

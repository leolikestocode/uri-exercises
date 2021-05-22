n, m = map(int, input().split())

for i in range(m):
    a = input()
    if (a == "fechou"):
        n += 1
    else:
        n -= 1

print(n)

a = list(map(int, input().split()))
a.sort()
print("S" if (a[0] + a[1]) > a[2] or (a[1] + a[2]) > a[3] else "N")

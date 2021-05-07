n = int(input())
s = 0
for i in range(n):
    x, y = input().split()
    if (x == "1001"):
        s += int(y) * 1.50
    elif (x == "1002"):
        s += int(y) * 2.50
    elif (x == "1003"):
        s += int(y) * 3.50
    elif (x == "1004"):
        s += int(y) * 4.50
    elif (x == "1005"):
        s += int(y) * 5.50

print("{:.2f}".format(s))

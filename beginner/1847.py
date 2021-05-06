a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if (b < a and c >= b):  # 1
    print(":)")
elif (b > a and c <= b):  # 2
    print(":(")
elif (b > a and c > b and c - b < b - a):  # 3
    print(":(")
elif (b > a and c > b and c - b >= b - a):  # 4
    print(":)")
elif (b < a and c < b and abs(c - b) < abs(b - a)):  # 5
    print(":)")
elif (b < a and c < b and abs(c - b) <= (b - a)):  # 6
    print(":(")
elif (b == a and c - b > b - a):  # 7
    print(":)")
else:
    print(":(")

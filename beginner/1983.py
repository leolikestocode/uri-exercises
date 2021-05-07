n = int(input())
high = 0
student = 0
for i in range(n):
    x, y = input().split()
    if (float(y) >= 8 and float(y) > high):
        student = int(x)
        high = float(y)

if (student == 0):
    print('Minimum note not reached')
else:
    print(student)

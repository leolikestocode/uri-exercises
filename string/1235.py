n = int(input())
for i in range(n):
    s = str(input())
    a, b = s[:len(s)//2], s[len(s)//2:]
    a = a[::-1]
    b = b[::-1]

    print(f'{a}{b}')

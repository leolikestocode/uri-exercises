n = int(input())

for i in range(n):
    x1, x2, y1, y2 = input().split()
    n1, n2 = input().split()

    is_par = (int(n1) + int(n2)) % 2 == 0

    print(x1 if is_par and x2 == "PAR" or not(
        is_par) and x2 == "IMPAR" else y1)

p, n = input().split()
arr = list(map(int, input().split()))
you_win = True

for i in range(0, int(n) - 1):
    if (abs(arr[i] - arr[i + 1]) > int(p)):
        you_win = False
        break

print('YOU WIN' if you_win else 'GAME OVER')

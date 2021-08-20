while 1:
  n, m = map(int, input().split())

  if n == 0 and m == 0:
    break

  sum = 0
  for i in range(n):
    team, points = input().split()
    sum = sum + int(points)

  print(m * 3 - sum)

n = int(input())
for i in range(n):
  sum_shots = 0
  shots = int(input())
  heights = list(map(int, input().split()))
  actions = list(input())

  for j in range(len(heights)):
    if ((actions[j] == "S" and (heights[j] == 1 or heights[j] == 2)) or actions[j] == "J" and heights[j] >= 3):
      sum_shots = sum_shots + 1

  print(sum_shots)

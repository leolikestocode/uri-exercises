def fatorial(n):
  if n == 0: return 1
  return n * fatorial(n - 1) 

while 1:
  n = input()

  if n == "0":
    break

  n = list(n[::-1])

  s = 0
  
  for i in range(len(n)):
    s = s + int(n[i]) * fatorial(i + 1)

  print(s)

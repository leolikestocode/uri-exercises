cases = 1
while 1:
  try:
    n = input()
    number_pairs = list(input().split())
    f = 0
    m = 0

    for i in range(int(len(number_pairs) / 2)):
      if (number_pairs[i * 2] == n):
        if (number_pairs[i * 2 + 1] == "F"):
          f = f + 1
        else: 
          m = m + 1

    if cases > 1:
      print()

    print(f'Caso {cases}:')
    print(f'Pares Iguais: {f + m}')
    print(f'F: {f}')
    print(f'M: {m}')
    
    cases = cases + 1

  except EOFError:
    break

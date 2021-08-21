while 1:
  try:
    vowels = list(input())
    phrase = list(input())
    sum_vowels = 0

    for letter in phrase:
      if letter in vowels:
        sum_vowels = sum_vowels + 1

    print(sum_vowels)

  except EOFError:
    break

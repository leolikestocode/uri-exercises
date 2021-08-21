word = input()
vowels_word = [i for i in word if i in "aeiou"]
is_funnier = True
count_back = len(vowels_word) - 1

for i in range(len(vowels_word)):
  if (vowels_word[i] != vowels_word[count_back]):
    is_funnier = False
    break

  count_back = count_back - 1

print("S" if is_funnier else "N")
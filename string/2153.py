while 1:
  try:
    word = input()
    word_list = list(word)
    back_clone_arr = []
    repetition_arr = []

    
    for i in range(len(word_list) - 1, -1, -1):
      back_clone_arr.insert(0, word[i])

      if (''.join(back_clone_arr) in word[0:i]):
        repetition_arr.insert(0, word[i])

    rep_len = len(repetition_arr)

    if (rep_len > 0 and word[(len(word_list) - 2 * rep_len):len(word_list) - rep_len] == ''.join(repetition_arr)):
      print(word[0:len(word_list) - rep_len])
    else:
      print(word)


  except EOFError:
    break

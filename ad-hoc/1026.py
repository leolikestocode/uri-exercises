while 1:
    words = str(input())
    if words == "*":
        break

    word_break = words.split(" ")

    first_letter = word_break[0][0].lower()

    for i in range(1, len(word_break)):
        if word_break[i][0].lower() != first_letter:
            print('N')
            break
    else:
        print("Y")

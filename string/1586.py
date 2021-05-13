def getPos(somaA, somaB, name_position):
    soma_pos = 1
    for i in range(n):
        if (i <= name_position):
            somaA += name_strength[i] * (name_position - i + 1)
        else:
            somaB += name_strength[i] * soma_pos
            soma_pos += 1

    return (somaA, somaB)


while 1:
    n = int(input())

    if (n == 0):
        break

    names = []
    name_strength = []

    for i in range(n):
        a = input()
        names.append(a)
        s = 0
        list_a = list(a)

        for j in list_a:
            s += ord(j)

        name_strength.append(s)
    name_position = int(n / 2) if n % 2 != 0 else int(n / 2) - 1

    somaA, somaB = getPos(0, 0, name_position)

    if (somaA == somaB):
        print(names[name_position])
    else:
        if somaA < somaB:
            operator = "sum"
            name_position += 1
        else:
            operator = "sub"
            name_position -= 1

        got_there = False
        sum_there = 0

        while (name_position != n and name_position != 0):

            somaA, somaB = getPos(0, 0, name_position)

            if (somaA == somaB):
                break

            if operator == "sum" and not(got_there):
                if (somaA > somaB):
                    got_there = True
                    name_position -= 1
                    item_there = name_position
                    operator = "sub"
                else:
                    name_position += 50

            elif not(got_there):

                if (somaA < somaB):
                    got_there = True
                    name_position += 1
                    item_there = name_position
                    operator = "sum"
                else:
                    name_position -= 50

            if (got_there):
                sum_there += 1
                if operator == "sum":
                    name_position += 1
                else:
                    name_position -= 1

            if (sum_there == 50):
                name_position = 0
                break

        if (name_position == n or name_position == 0):
            print('Impossibilidade de empate.')
        else:
            print(names[name_position])

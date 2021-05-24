while 1:
    try:
        n = int(input())
        custoPorDia = int(input())
        receita = []

        for i in range(n):
            receita.append(int(input()))

        maior = 0
        for i in range(n):
            s_item = 0
            s_atual = 0
            for j in range(i, n):
                s_item += 1
                s_atual += receita[j]

                s = s_atual - custoPorDia * s_item
                if (s > maior):
                    maior = s

        print(maior)

    except EOFError:
        break

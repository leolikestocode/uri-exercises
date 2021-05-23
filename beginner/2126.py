caso = 1

while 1:
    try:
        n1 = input()
        n2 = input()
        qt = n2.count(n1)

        print('Caso #%d:' % caso)
        if qt == 0:
            print('Nao existe subsequencia')

        else:
            print('Qtd.Subsequencias: %d' % qt)

            qt = n2.rfind(n1)
            print('Pos: %d' % (int(qt)+1))
        print()
        caso += 1

    except EOFError:
        break

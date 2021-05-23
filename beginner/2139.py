from datetime import date

while 1:
    try:
        m, d = map(int, input().split())

        f_date = date(2016, m, d)
        l_date = date(2016, 12, 25)

        diff = (l_date - f_date).days

        if (diff == 1):
            print('E vespera de natal!')
        elif (diff == 0):
            print('E natal!')
        elif (diff > 1):
            print('Faltam {} dias para o natal!'.format(diff))
        else:
            print('Ja passou!')

    except EOFError:
        break

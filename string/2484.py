while 1:
    try:
        n = list(input())
        passed = 0
        for i in range(0, len(n)):
            for j in range(0, len(n) - passed):
                print(n[j], end='')

                if (j + 1 < len(n) - passed):
                    print(' ', end='')
            print('')
            passed += 1
            if (i + 1 < len(n)):
                print(' ' * passed, end='')
        print('')

    except EOFError:
        break

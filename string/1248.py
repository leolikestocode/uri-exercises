n = int(input())

for i in range(n):
    a = list(input())
    b = list(input())
    c = list(input())

    if (len(list(set(b) - set(a))) or len(list(set(c) - set(a)))):
        print('CHEATER')
    else:
        rest = list(set(a) - set(b) - set(c))

        rest.sort()
        print("".join(rest))

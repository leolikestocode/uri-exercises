N = input()

while N != "0 0":
    X, Y = N.split()
    M = input()
    obj = {}

    for i in M.split():
        if i in obj:
            obj[i] = obj[i] + 1
        else:
            obj[i] = 1

    sumFake = 0
    for _, v in obj.items():
        if v > 1:
            sumFake += 1

    print(sumFake)

    N = input()

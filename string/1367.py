while 1:
    n = int(input())

    if (n == 0):
        break

    incorrect = {}
    sum_correct = 0
    sum_final = 0

    for i in range(n):
        a, b, c = input().split()

        if (c == "incorrect"):
            if (a in incorrect):
                incorrect[a] += 20
            else:
                incorrect[a] = 20

        if (c == "correct"):
            if (not(a in incorrect)):
                incorrect[a] = 0

            sum_final += int(b) + incorrect[a]
            sum_correct += 1

    print(sum_correct, sum_final)

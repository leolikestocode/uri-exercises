
def getFib():
    n = 63245986  # valor de fibonnaci 39
    t1 = 0
    t2 = 1
    t3 = 0

    fib = []

    while t3 <= n:
        fib.append(t3)
        t3 = t1 + t2
        t1 = t2
        t2 = t3

    return fib


def getCallsFib():
    n = 204668308  # valor de calls para fibonnaci 39
    t2 = 2
    t3 = 4
    t4 = 8
    t5 = 0

    fib = [0, 2]

    while t5 <= n:
        fib.append(t3)
        t5 = t4 * 2 - t2
        t2 = t3
        t3 = t4
        t4 = t5

    fib.append(204668308)

    return fib


fib_numbers = getFib()
fib_calls = getCallsFib()

n = int(input())

for i in range(n):
    x = int(input())

    print('fib({}) = {} calls = {}'.format(
        x, fib_calls[x - 1], fib_numbers[x - 1]))

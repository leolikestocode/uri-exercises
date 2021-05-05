from collections import deque


def removeInIndex(people, primes):
    de = deque(people)
    index = 0
    while len(de) > 1:
        de.rotate(-primes[index])
        de.pop()
        index += 1
    return(de.pop())


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


n = int(input())
# Get first 3501 index of primes
primes = get_primes(32620)

while n:
    if (n == 0):
        break
    people = [x for x in range(1, int(n)+1)]
    result = removeInIndex(people, primes)
    print(result)

    n = int(input())

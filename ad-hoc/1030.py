from collections import deque


def removeInIndex(people, jump):
    de = deque(people)
    while len(de) > 1:
        de.rotate(-jump)
        de.pop()
    return(de.pop())


n = int(input())
for i in range(n):
    people, jump = input().split()
    people = [x for x in range(1, int(people)+1)]
    jump = int(jump)
    result = removeInIndex(people, jump)
    print('Case %d: %d' % (i+1, result))

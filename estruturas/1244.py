n = int(input())

for i in range(n):
    n = list(input().split())

    n.sort(reverse=True, key=lambda e: len(e))

    print(' '.join(n))

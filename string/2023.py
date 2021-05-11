kid = []

while True:
    try:
        kid.append(input())

    except EOFError:
        kid = sorted(kid, key=lambda s: s.lower())
        print(kid[len(kid) - 1])
        break

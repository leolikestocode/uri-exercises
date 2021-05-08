s, t, f = map(int, input().split())

soma = s + t + f

print(soma if soma < 24 and soma >= 0 else soma + 24 if soma < 0 else soma % 24)

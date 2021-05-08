p, j1, j2, r, a = map(int, input().split())

soma = j1 + j2

if (soma % 2 == 0):
    parimpar = 0
else:
    parimpar = 1


if (p == 1 and parimpar == 0 and r == 0 and a == 0):  # p == 1 par jogador 1
    print("Jogador 1 ganha!")
elif (p == 0 and parimpar == 1 and r == 0 and a == 0):  # p ==0 impar jogador 1
    print("Jogador 1 ganha!")
elif (r == 1 and a == 0):  # Jogador 1 roubou
    print("Jogador 1 ganha!")
elif (r == 1 and a == 1):  # Acusou o roubo
    print("Jogador 2 ganha!")
elif (p == 1 and parimpar == 1 and r == 0 and a == 0):
    print("Jogador 2 ganha!")
elif (p == 0 and parimpar == 0 and r == 0 and a == 0):
    print("Jogador 2 ganha!")
elif (r == 0 and a == 1):
    print("Jogador 1 ganha!")

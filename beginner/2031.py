n = int(input())

for i in range(n):
    j1 = input()
    j2 = input()

    print(j1, j2)

    if (j1 == "ataque" and j2 == "ataque"):
        print("Aniquilacao mutua")
    elif (j1 == "pedra" and j2 == "pedra"):
        print("Sem ganhador")
    elif (j1 == "papel" and j2 == "papel"):
        print("Ambos venceram")
    elif ((j1 == "ataque" and j2 == "pedra" or j2 == "papel") or (j1 == "pedra" and j2 == "papel")):
        print("Jogador 1 venceu")
    elif ((j2 == "ataque" and j1 == "pedra" or j1 == "papel") or (j2 == "pedra" and j1 == "papel")):
        print("Jogador 2 venceu")

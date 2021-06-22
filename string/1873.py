n = int(input())

for i in range(n):
    a, b = input().split()

    if (
        a == "tesoura" and b == "papel" 
        or a == "papel" and b == "pedra"
        or a == "pedra" and b == "lagarto"
        or a == "lagarto" and b == "spock"
        or a == "spock" and b == "tesoura"
        or a == "tesoura" and b == "lagarto"
        or a == "lagarto" and b == "papel"
        or a == "papel" and b == "spock"
        or a == "spock" and b == "pedra"
        or a == "pedra" and b == "tesoura"
    ):
        print("rajesh")
    elif (
        b == "tesoura" and a == "papel" 
        or b == "papel" and a == "pedra"
        or b == "pedra" and a == "lagarto"
        or b == "lagarto" and a == "spock"
        or b == "spock" and a == "tesoura"
        or b == "tesoura" and a == "lagarto"
        or b == "lagarto" and a == "papel"
        or b == "papel" and a == "spock"
        or b == "spock" and a == "pedra"
        or b == "pedra" and a == "tesoura"
    ):
        print("sheldon")
    else:
        print("empate")
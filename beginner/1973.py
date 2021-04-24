n = int(input())
n2 = input()

n2 = map(int, n2.split())
ataques = 0
index = 0
not_end = True

while(not_end):
    if (n2[index] % 2 == 0):
        n2[index] -= 1
        index -= 1
    else:
        n2[index] -= 1
        index += 1

    if (index == -1 or index == len(n2) or n2[index] == 0):
        not_end = False

    if (index != len(n2) and index > ataques):
        ataques = index

print(ataques + 1, sum(n2))

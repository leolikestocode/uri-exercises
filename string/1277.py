n = int(input())

for i in range(n):
    s = int(input())
    students = list(input().split())
    registers = list(input().split())

    final = []

    for j in range(s):
        no_M = registers[j].replace('M', '')
        no_M_and_A = no_M.replace('A', '')
        total = len(no_M)
        present = len(no_M_and_A)

        if ((present / total) < 0.75):
            final.append(students[j])

    print(" ".join(final))

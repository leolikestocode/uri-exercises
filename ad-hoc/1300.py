deg = ["Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y","N","N","N","N","N","Y"]


while 1:
    try:
        n = int(input())

        print(deg[n])

    except EOFError:
        break
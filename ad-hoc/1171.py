m = int(input())
obj = {}

for j in range(m):
    n = int(input())

    if n in obj:
        obj[n] = obj[n] + 1
    else:
        obj[n] = 1

newObj = sorted(obj)

for i in newObj:
    print(f"{i} aparece {obj[i]} vez(es)")

times = int(input())

for i in range(0, times):
    items = int(input())
    split_items = items.split(' ')

    item1 = split_items[0]
    item2 = split_items[i]

    print(item1, item2)

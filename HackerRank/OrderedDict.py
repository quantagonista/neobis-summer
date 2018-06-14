from collections import OrderedDict

N = int(input())
ordDict = OrderedDict()
for _ in range(N):
    row = input().split(' ')
    price = int(row.pop(-1))
    item_name = ' '.join(row)
    if item_name in ordDict:
        ordDict[item_name] += price
    else:
        ordDict[item_name] = price

for item in ordDict.items():
    print(item[0], item[1])


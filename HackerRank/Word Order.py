from collections import OrderedDict

N = int(input())
ordDict = OrderedDict()
distinct = 0
for _ in range(N):
    item_name = input()
    if item_name in ordDict:
        ordDict[item_name] += 1

    else:
        distinct += 1
        ordDict[item_name] = 1

row = ' '.join([str(x) for x in ordDict.values()])
print(distinct)
print(row)


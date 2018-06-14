#!/bin/python3

import re

nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix_item.replace('', ' ')
    matrix.append(list(matrix_item))
output = ''

for i in range(m):
    output += ''.join([x[i] for x in matrix])

output = re.sub(r'(?<=[\w])[\W]+(?=[\w])', ' ', output)

print(output)

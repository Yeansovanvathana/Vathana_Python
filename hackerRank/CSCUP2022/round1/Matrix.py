
import numpy as np

matrixA_rows = int(input().strip())
matrixA_columns = int(input().strip())

matrixA = []

for _ in range(matrixA_rows):
    matrixA.append(list(map(int, input().rstrip().split())))

matrixB_rows = int(input().strip())
matrixB_columns = int(input().strip())

matrixB = []

for _ in range(matrixB_rows):
    matrixB.append(list(map(int, input().rstrip().split())))

row = matrixA_rows
col = matrixB_columns
result = []
for i in range(row):
    k = []
    for j in range(col):
        k.append(0)
    result.append(k)

for i in range(len(matrixA)):

    # iterating by column by B
    for j in range(len(matrixB[0])):

        # iterating by rows of B
        for k in range(len(matrixB)):
            result[i][j] += matrixA[i][k] * matrixB[k][j]

for ans in result:
    print('  '.join(map(str, ans)))
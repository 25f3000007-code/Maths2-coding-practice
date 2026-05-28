import math
n = int(input("Enter the matrix size: "))
matrix = []

for i in range(1, n+1):
    row = []
    for j in range(1,n+1):
        a = math.sin(i) + math.cos(j)
        row.append(a)
    matrix.append(row)

print(matrix)
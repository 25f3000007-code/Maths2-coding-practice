import math
n = int(input("Enter the matrix size: "))
row1 = []
row2 = []
row3 = []

for j in range (1, n+1):
    row1_a = math.sin(1) + math.cos(j)
    row1.append(row1_a)
    row2_a = math.sin(2) + math.cos(j)
    row2.append(row2_a)
    row3_a = math.sin(3) + math.cos(j)
    row3.append(row3_a)
    
matrix = [row1, row2, row3,]

print(matrix)
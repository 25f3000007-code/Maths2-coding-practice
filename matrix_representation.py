import math
n = int(input("Enter the matrix size: "))
matrix = []

for i in range(1, n+1):
    row = []
    for j in range(1,n+1):
        a = math.sin(i) + math.cos(j)
        row.append(a)
    matrix.append(row)

# better representation
for row in matrix:                                                              #The key idea is:
    for element in row:                                                         #for row in matrix → move down the matrix./for element in row → move across the matrix./end=" " → stay on the same line./print() after the inner loop → start a new row.
        print(f"{element:.3f}", end = " ")
    print() # an empty print means  = print("\n")
    
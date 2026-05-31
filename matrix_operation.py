rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix1 = []
matrix2 = []
for i in range(1, rows+1):
    r = (input(f'Enter row{i} of Matrix 1: ').split())
    matrix1.append(r)

for i in range(1, rows+1):
    r = (input(f'Enter row{i} of Matrix 2: ').split())
    matrix2.append(r)
    
A = matrix1
B = matrix2 
def matrix_addition(A, B):
    sum_matrix = []
    for i in range(0, rows):
        for j in range(0, columns):
            r = int(A[i][j])+int(B[i][j])
            sum_matrix.append(r)
    
      
    
    return(sum_matrix)

print(matrix_addition(A,B))

def matrix_subtraction(A, B):
    dif_matrix = []
    for i in range(0, rows):
        for j in range(0, columns):
            r = int(A[i][j])-int(B[i][j])
            dif_matrix.append(r)
    
      
    
    return(dif_matrix)

print(matrix_subtraction(A,B))

def largest_element(A,B):
    eA = 0
    eB = 0
    # for matrix A 
    for i in range(0, rows):
        for j in range(0,rows):
            if int(A[i][j]) > eA:
                eA = int(A[i][j])
    for i in range(0, rows):
        for j in range(0,rows):
            if int(B[i][j]) > eB:
                eB = int(B[i][j])
    return(f' Max among both the matrix is {max(eA,eB)} and for Matrix A it is {eA} and for matrix B is {eB}')


def smallest_element(A,B):
    eA = 999999999999999999999999999999999999999
    eB = 999999999999999999999999999999999999999
    # for matrix A 
    for i in range(0, rows):
        for j in range(0,rows):
            if int(A[i][j]) < eA:
                eA = int(A[i][j])
    for i in range(0, rows):
        for j in range(0,rows):
            if int(B[i][j]) < eB:
                eB = int(B[i][j])
    return(f' Min among both the matrix is {min(eA,eB)} and for Matrix A it is {eA} and for matrix B is {eB}')

print(largest_element(A,B))
print(smallest_element(A,B))
'''Problem Statement: Matrix Type Identifier
    Write a Python program that takes a matrix as input from the user and determines whether it is:
        A Square Matrix
        A Diagonal Matrix
        A Scalar Matrix'''
        
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix = []
for i in range(1, rows+1):
    r = (input(f'Enter row{i}: ').split())
    matrix.append(r)

    
def diagonal_and_non_diognal_elements():
    non_diagonal = []
    diagonal = []
    for i in range(0, rows):
        for j in range(0, columns):
            if i != j:
                non_diagonal.append(matrix[i][j])
            else:
                diagonal.append(matrix[i][j])
    return(diagonal,non_diagonal)

x = diagonal_and_non_diognal_elements()

argument1  = x[0]
argument2 = x[1]


               


def upper_triangular(matrix):
    lower_element = []
    for i in range(1, rows):
        for j in range(0, i):
            lower_element.append(matrix[i][j])
    return(lower_element)

arguement3 = upper_triangular(matrix)
                        
def matrix_check(diagonal, non_diagonal, lower_element):
    square_matrix = rows == columns
    diagonal_matrix = False
    scalar_matrix = False
    upper_triangular = False

    if square_matrix and all(item == "0" for item in non_diagonal):
        diagonal_matrix = True
        target = diagonal[0]
        scalar_matrix = all(item == target for item in diagonal)
    if square_matrix:
        upper_triangular = all(item == '0' for item in lower_element)

    return(f'Square Matrix: {square_matrix}\nDiagonal Matrix: {diagonal_matrix}\nScalar Matrix: {scalar_matrix}\nUpper Triangular Matrix: {upper_triangular}')

print(matrix_check(argument1, argument2, arguement3))
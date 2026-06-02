# Read matrix dimensions from the user. These determine how many rows and columns each matrix will have.
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Prepare two empty lists that will store the rows for each input matrix.
matrix1 = []
matrix2 = []

# Read each row of the first matrix.
for i in range(1, rows + 1):
    # The user enters a row as space-separated numbers.
    r = input(f'Enter row{i} of Matrix 1: ').split()
    # Append the row (as a list of strings) to matrix1.
    matrix1.append(r)

# Read each row of the second matrix.
for i in range(1, rows + 1):
    r = input(f'Enter row{i} of Matrix 2: ').split()
    matrix2.append(r)

# Assign the input matrices to variables A and B for convenience.
A = matrix1
B = matrix2

# Compute the element-wise sum of two matrices.
def matrix_addition(A, B):
    # This function returns a flat list of sums in row-major order.
    sum_matrix = []
    for i in range(rows):
        for j in range(columns):
            # Convert each element to int and add corresponding elements.
            r = int(A[i][j]) + int(B[i][j])
            sum_matrix.append(r)
    return sum_matrix

# Call the addition function and store its result in add.
add = matrix_addition(A, B)

# Compute the element-wise difference of two matrices.
def matrix_subtraction(A, B):
    # This function returns a flat list of differences in row-major order.
    dif_matrix = []
    for i in range(rows):
        for j in range(columns):
            r = int(A[i][j]) - int(B[i][j])
            dif_matrix.append(r)
    return dif_matrix

# Call the subtraction function and store its result in dif.
dif = matrix_subtraction(A, B)

# Find the largest element in each matrix and compare them.
def largest_element(A, B):
    # Initialize maximum values for A and B.
    eA = 0
    eB = 0

    # Loop over every element in matrix A.
    for i in range(rows):
        for j in range(rows):
            if int(A[i][j]) > eA:
                eA = int(A[i][j])

    # Loop over every element in matrix B.
    for i in range(rows):
        for j in range(rows):
            if int(B[i][j]) > eB:
                eB = int(B[i][j])

    # Return a formatted message with the maxima.
    return (f' Max among both the matrix is {max(eA, eB)} and for Matrix A it is {eA} and for matrix B is {eB}')

# Find the smallest element in each matrix and compare them.
def smallest_element(A, B):
    # Start with very large values so any real matrix entry will be smaller.
    eA = 999999999999999999999999999999999999999
    eB = 999999999999999999999999999999999999999

    # Check every element in matrix A.
    for i in range(rows):
        for j in range(rows):
            if int(A[i][j]) < eA:
                eA = int(A[i][j])

    # Check every element in matrix B.
    for i in range(rows):
        for j in range(rows):
            if int(B[i][j]) < eB:
                eB = int(B[i][j])

    # Return a formatted message with the minima.
    return (f' Min among both the matrix is {min(eA, eB)} and for Matrix A it is {eA} and for matrix B is {eB}')

# Print the matrix addition result row by row using the flat list add.
print("Matrix addition:")
for i in range(rows):
    # Compute start and end indices for the current row in the flat list.
    start = i * columns
    end = start + columns
    row = add[start:end]
    # Join the row values into a single string separated by spaces.
    print(" ".join(str(x) for x in row))

# Print the matrix subtraction result row by row using the flat list dif.
print("Matrix subtraction:")
for i in range(rows):
    start = i * columns
    end = start + columns
    row = dif[start:end]
    print(" ".join(str(x) for x in row))

# Print the largest and smallest element information.
print(largest_element(A, B))
print(smallest_element(A, B))

# Print the sum of each column as its own list.
def column_addition(A, B):
    for j in range(columns):
        col = []
        for i in range(rows):
            val = int(A[i][j]) + int(B[i][j])
            col.append(val)
        print(f'Column {j} addition is {col}')

# Print the sum of each row as its own list.
def row_addition(A, B):
    for i in range(rows):
        row = []
        for j in range(columns):
            val = int(A[i][j]) + int(B[i][j])
            row.append(val)
        print(f'Row {i} addition is {row}')

# Call the helper functions to display row-based and column-based sums.
column_addition(A, B)
row_addition(A, B)

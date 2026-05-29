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
    
print(matrix)     
def get_diagonal():
    diagonal = [] 
    for i in range(0, rows):
        temp_list = matrix[i]
        element = temp_list[i]
        diagonal.append(element)
    return(diagonal)

print(get_diagonal())

'''You loop with for i in range(1, rows+1):
Python lists are zero-indexed, so valid row indices are 0 to rows-1
When i == rows, matrix[i] is out of range and raises IndexError'''

    



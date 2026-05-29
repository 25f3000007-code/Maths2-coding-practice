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



    



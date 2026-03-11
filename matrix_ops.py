def matrix_add(A, B):

    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result

def matrix_multiply(A,B):

    result = [[sum(a*b for a,b in zip(row,col))
               for col in zip(*B)]
               for row in A]

    return result

def matrix_transpose(matrix):

    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def matrix_multiply(A,B):

    result = [[sum(a*b for a,b in zip(row,col))
               for col in zip(*B)]
               for row in A]

    return result

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

print(matrix_add(a,b))
print(matrix_transpose(a))
print(matrix_multiply(a,b))
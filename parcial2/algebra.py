def identity_matrix(n):
    L = [[0] * n for i in range(n)]
    for i in range(n):
        L[i][i] = 1
    return L

def copy_matrix(M):
    L = [[0] * len(M[0]) for i in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            L[i][j] = M[i][j]
    return L

def matrix_multiply(a, b):
    to_return = []
    for i in range(len(a)):
        to_return.append([])
        for j in range(len(b[0])):
            to_return[i].append(0)
            for k in range(len(b)):
                to_return[i][j] += a[i][k] * b[k][j]
    return to_return

# Invert a matrix using Gauss-Jordan elimination
def matrix_invert(a):
    n = len(a)
    # Create the identity matrix, and a copy of the original
    a = copy_matrix(a)
    b = identity_matrix(n)
    # Perform elementary row operations
    for i in range(n):
        # Get the element with the largest absolute value
        max = abs(a[i][i])
        max_row = i
        for j in range(i+1, n):
            if abs(a[j][i]) > max:
                max = abs(a[j][i])
                max_row = j
        # Swap the row with the highest value with the current row
        (a[i], a[max_row]) = (a[max_row], a[i])
        (b[i], b[max_row]) = (b[max_row], b[i])
        # Make all rows below this one 0 in the first column
        for j in range(i+1, n):
            c = a[j][i] / a[i][i]
            for k in range(n):
                a[j][k] -= a[i][k] * c
                b[j][k] -= b[i][k] * c
    # Make all rows above this one 0 in the first column
    for i in range(n-1, 0, -1):
        c = a[i-1][i] / a[i][i]
        for j in range(n):
            a[i-1][j] -= a[i][j] * c
            b[i-1][j] -= b[i][j] * c
    # Scale the matrix to make it an identity matrix
    for i in range(n):
        c = a[i][i]
        for j in range(n):
            a[i][j] /= c
            b[i][j] /= c
    return b

def vectorial_product(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

def transpose_matrix(M):
    to_return = []
    for i in range(len(M[0])):
        to_return.append([])
        for j in range(len(M)):
            to_return[i].append(M[j][i])
    return to_return

def solve_system(A, b):
    return matrix_multiply(matrix_invert(A), b)

def minor(M, i, j):
    to_return = []
    for k in range(len(M)):
        if k != i:
            to_return.append([])
            for l in range(len(M[0])):
                if l != j:
                    to_return[-1].append(M[k][l])
    return to_return

def determinant(M):
    if len(M) == 1:
        return M[0][0]
    else:
        to_return = 0
        for i in range(len(M)):
            to_return += M[0][i] * determinant(minor(M, 0, i)) * (-1)**i
        return to_return

# testsuite
if __name__=='__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
    b = [[1], [2], [3]]
    print(solve_system(A, b))
    print(determinant(A))
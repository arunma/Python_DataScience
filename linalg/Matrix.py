def shape(A):
    num_rows=len(A)
    num_cols=len(A[0])
    return num_rows, num_cols

def get_row(A, i):
    return A[i]


def get_column(A,i):
    return [ARow[i] for ARow in A]

matrix_1=[[1,2,3],
          [4,5,6]]

matrix_2=[[1,2],
          [3,4],
          [5,6]]


print (shape(matrix_1))

print (get_row(matrix_1, 0))

print (get_column (matrix_1, 1))

print [aRow for aRow in matrix_1]


def make_matrix(num_rows, num_columns, entry_fn):
    """
    creates a num_rows * num_columns matrix whose (i,j) entry is an entry_fn
    """
    return [[entry_fn(i, j) for j in range(num_columns)] for i in range(num_rows)]

def diagonal(i, j):
    return 1 if i==j else 0

identity_matrix= make_matrix(5,5, diagonal)




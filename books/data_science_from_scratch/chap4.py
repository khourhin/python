from functools import partial, reduce
import math

# This is made for exposition purposes !
# Plenty of those function are implemented (and better !)
# in the numpy module


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


def vector_sum_old(vectors):
    """sums all corresponding elements"""
    # start with the first vector_add 
    result = vectors[0]
    # then loop over the others
    for vector in vectors[1:]:
        # and add them to the result
        result = vector_add(result, vector)
    return result


def vector_sum(vectors):
    # Same as the one before but much more clever
    # And functionnal programming style
    return reduce(vector_add, vectors)

# or even
# vector_sum = partial(reduce, vector_add)


def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""

    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """
    v_1 * v_1 + ... + v_n * v_n
    """
    return dot(v, v)


def magnitude(v):
    """ie the size of a vector"""
    return math.sqrt(sum_of_squares(v))


def distance(v, w):
    """
    Distance betweeen two vectors
    """
    return magnitude(vector_subtract(v, w))


def shape(A):
    """
    Statistics on the shape of a matrix A
    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   # number of elements in first row
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_col(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """
    returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)
             for i in range(num_rows)]]
    

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)



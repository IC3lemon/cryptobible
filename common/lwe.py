from sage.all import *

def lwe(A, b, p):
    """
    A * s + e = b (mod p)
    given matrix A (m x n) of n eqns with m unknowns, b = [b_i ... ]
    returns list [e_i ... ]
    for small errors e
    """
    A = A.change_ring(ZZ)
    b = b.change_ring(ZZ)
    M = Matrix(ZZ, list(b), sparse=False)
    M = M.stack(Matrix(ZZ, A.T, sparse=False)) 
    M = M.stack(diagonal_matrix(ZZ, [p] * A.nrows(), sparse=False)) 
    L = M.LLL()
    for i in L:
        print(f"{i}\n")

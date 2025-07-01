from sage.all import *

def lwe(A, b, p):
    """
    A * s + e = b (mod p)
    given matrix A (m x n) of n eqns with m unknowns, b = [b_i ... ]
    returns list [e_i ... ]
    for small errors e
    Args:
        A : m x n matrix of n eqns with m unkowns
        b : n degree vector
        p : modulus

    Returns:
        e : n degree error vector
    """
    A = A.change_ring(ZZ)
    b = b.change_ring(ZZ)
    M = Matrix(ZZ, list(b), sparse=False)
    M = M.stack(Matrix(ZZ, A.T, sparse=False)) 
    M = M.stack(diagonal_matrix(ZZ, [p] * A.nrows(), sparse=False)) 
    L = M.LLL()
    for i in L:
        if i != 0:
            break
    return i

def test():
    p = 1361
    m, n = 60, 30
    A = random_matrix(GF(p), m, n)
    s = random_vector(GF(p), n)
    e = vector([randint(-1, 1) for i in range(m)])
    b = A*s + e
    # print(f"{e = }")
    
    assert e or -e in lwe(A, b, p) # should have e

if __name__ == "__main__":
    test()
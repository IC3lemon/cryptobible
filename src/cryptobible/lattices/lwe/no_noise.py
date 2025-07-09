from sage.all import *

def lwe_no_noise(A,b,p):
    """
    b = A*s mod p
    given matrix A (n x n) of n unknowns and n equations and n degree vector b, solves for the secret s(n degree vector) provided there is no error term
    Args:
        A: n x n matrix of n unknowns and n equations
        b: n degree vector
        p: modulus

    Returns:
        s: n degree secret vector
    """
    A = A.change_ring(GF(p))
    b = b.change_ring(GF(p))
    s = A.solve_right(b)
    return s


def test():
    p = 1361
    n = 64
    A = random_matrix(GF(p), n, n)
    s = random_vector(GF(p), n)
    b = A*s
    assert s == lwe_no_noise(A,b,p)

if __name__ == "__main__":
    test()
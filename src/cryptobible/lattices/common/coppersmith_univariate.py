from sage.all import *

def coppersmith(coefficients : list, degree : int, n, UB, beta=0.5):
    """
    Coppersmith's univariate

    Args:
        coeffs : list of coefficients
        degree : degree of the polynomial
        n : modulus
        UB : upper bounds for the unkown
        beta : make beta smaller in case of higher degree of f

    Returns:
        roots : roots to the eqn
    """
    R = PolynomialRing(Zmod(n), 'x')
    x = R.gen()
    f = 0
    for i in range(len(coeffs)):
        f += coeffs[i] * x**i
    
    roots = f.monic().small_roots(X=UB, beta=beta)

    return roots

def test(degree=3, N_bits=512):
    N = random_prime(2**N_bits)
    root = randint(1, 2**(N_bits // 5))
    UB = 2**(root.bit_length() + 1)
    coeffs = [randint(0, N-1) for _ in range(degree)]

    R = PolynomialRing(Zmod(N), 'x')
    x = R.gen()
    f = x**degree
    for i in range(degree):
        f += coeffs[i] * x**i

    f_val = f(root)
    f = f - f_val
  
    assert root in coppersmith(f.coefficients(), degree, N, UB)
    
if __name__ == "__main__":
    test()
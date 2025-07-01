from sage.all import *

# also demonstrated at sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots
# knowing upper bits of p / q can help in factoring n faster
# say _p = upper 824 bits of a 1024 bit p
# then p = _p << 200 + x
# where x is lower 200 bits of p

# to find x, given n, we can create a function
# f(x) = x + _p << 200 (mod p || q)
# roots of above function are satisfied only when rhs is p (mod p || q) i.e. 0
# thus roots of this equation yield lower 200 bits of p
# make sure to have bounds set and an accurate beta, and the fact that the size of the missing root is correctly adjusted acc to degree(which is 1 in this case ig)

def coppersmith_factor(N : int, _p : int, n: int):
    """
    Factors n = p*q given upper bits of one of the factors

    Args:
        N : given modulus
        _p : upper '1024 - n' bits, for a 1024 bit prime
        n : number of missing bits
    """
    R = PolynomialRing(Zmod(N), 'x')
    x = R.gen()

    f = x + _p*2**n
    lsb = (f.monic().small_roots(X=2**n, beta=0.4))[0]
    p = int( lsb + _p*2**n ) # succesfully got p
    q = N // p # successfully factored p, q

    return p, q

def test():
    p, q = random_prime(2**1024), random_prime(2**1024)
    N = p*q
    _p = p >> 200
    p_, q_ = coppersmith_factor(N, _p, 200)

    assert p_ == p and q_ == q

if __name__ == "__main__":
    test()


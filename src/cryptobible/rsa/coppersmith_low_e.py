from sage.all import *
from os import *
from Crypto.Util.number import *

def split_at_nulls(s):
    i = s.find(b'\x00')
    if i == -1:
        return (s, b'', b'')  # no nulls

    # Find end of the null run
    j = i
    while j < len(s) and s[j] == 0:
        j += 1

    return s[:i], s[i:j], s[j:]


def coppersmith_low_e(n, e, c, known):
    """
    c = m**e % n
    given patterns in m (such as m = x + known) and that exponent is low, solves the polynomial
    (x + known)**e - c = 0 (mod n)

    Args:
        n : modulus
        e : some low number like 3
        c : ciphertext
        known : a bytestring with \x00's for the unkown chars

    Returns:
        x : unkown part of the message

    this script fails if the known has \x00's that arent coupled, need to cook a coppersmiths bivariate for that
    """
    R = PolynomialRing(Zmod(n), 'x')
    x = R.gen()
    A, B, C = split_at_nulls(known)

    f = (x*256**(len(C)) + bytes_to_long(known))**3 - c 
    roots = f.monic().small_roots(X=256**(len(B)), beta=0.5)
    return long_to_bytes(int(roots[0]))

def test():
    secret = urandom(6)
    m = bytes_to_long(b'flag{' + secret + b'}' + b'a'*69)
    e = 3
    p, q = getPrime(1024), getPrime(1024)
    n = p * q

    c = pow(m, e, n)
    known = b'flag{' + b'\x00'*6 + b'}' + b'a'*69
    assert secret == coppersmith_low_e(n, e, c, known)
    
if __name__ == "__main__":
    test()
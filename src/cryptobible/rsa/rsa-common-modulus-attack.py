from Crypto.Util.number import *
from sympy import *
from functools import reduce
import gmpy2
# from sage.all import *

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def common_modulus_attack(c1 : int, c2 : int, e1 : int, e2 : int, N : int) -> int:
    """
    Attack to be used when SAME MESSAGE has been encrypted with SAME MODULUS, but different public exponents
    the public exponents must be coprime

    refer to github.com/IC3lemon/cryptobible/tree/main/RSA#common-modulus-attack
    for details on how the attack works
    
    Args:
        c1: First ciphertext
        e1: First public exponent
        c2: Second ciphertext
        e2: Second public exponent
        N: common modulus
        
    """
    _gcd, a, b = extended_gcd(e1, e2)
    if _gcd != 1:
        raise ValueError("public exponents are not coprime.")
    
    if a < 0:
        a *= -1
        c1 = pow(c1, -1, N)
    if b < 0:
        b = -b
        c2 = pow(c2, -1, N)

    m = pow(c1, a, N) * pow(c2, b, N) % N
    return m


if __name__ == "__main__":
    c1=    # ciphertext 1
    c2=    # ciphertext 2
    e1=    # public exponent 1
    e2=    # public exponent 2
    n=     # common modulus
    m = common_modulus_attack(c1, c2, e1, e2, n)
    print(f"flag : {long_to_bytes(m)}")

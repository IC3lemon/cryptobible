from sage.all import *

def xgcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = xgcd(b % a, a)
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
        
    Returns:
        m : message
    """
    _gcd, a, b = xgcd(e1, e2)
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

def test():
    n = random_prime(2**512) * random_prime(2**512)
    m = randint(0, 2**128)
    e1, e2 = random_prime(2**16), random_prime(2**16)
    c1, c2 = pow(m, e1, n), pow(m, e2, n)

    assert m == common_modulus_attack(c1, c2, e1, e2, n)

if __name__ == "__main__":
    test()

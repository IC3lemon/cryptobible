from Crypto.Util.number import *

'''
c1 = m ** e1  % n
c2 = m ** e2  % n

e1, e2 are coprime
'''

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def common_modulus_attack(c1 : int, c2 : int, e1 : int, e2 : int, N : int) -> int:
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

c1 = 
c2 =
e1 =
e2 =
n =
decrypted = common_modulus_attack(c1, c2, e1, e2, n)
print(long_to_bytes(decrypted))

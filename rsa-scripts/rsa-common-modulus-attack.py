from Crypto.Util.number import *
from sympy import mod_inverse

"""
c1 = m ** e1  % n
c2 = m ** e2  % n
"""

c1 = # ciphertext 1
c2 = # ciphertext 2
e1 = # exponent 1
e2 = # exponent 2
n = # modulus

def attack(c1, c2, e1, e2, N):
    g = GCD(e1, e2)
    if g != 1:
        print("exponents aint coprime")
        return

    s1 = mod_inverse(e1, e2)
    s2 = (g - e1 * s1) // e2

    temp = mod_inverse(c2, N)
    m1 = pow(c1, s1, N)
    m2 = pow(temp, -s2, N)
    r1 = (m1 * m2) % N

    return r1

print(long_to_bytes(attack(c1,c2,e1,e2,n)))

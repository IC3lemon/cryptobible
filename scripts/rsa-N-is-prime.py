from Crypto.Util.number import *

#  ----------rsa when N is prime----------

#  Thine must have sympy and pycryptodome modules installed for this to worketh.


e = 65537 
N = 69696969696969 # N WHICH IS PRIME
ct = b'encoded' # thine ciphertext in bytes
c = bytes_to_long(ct) # thine ciphertext in long

# Function extracted from https://hackmd.io/@65XZ9ZfDTb21FI-0un6Zhg/BJj1FqYUK#Defective-RSA
def roots_of_unity(e, phi, n, rounds=500):
    phi_coprime = phi
    while GCD(phi_coprime, e) != 1:
        phi_coprime //=  GCD(phi_coprime, e)

    roots = set(pow(i, phi_coprime, n) for i in range(1, rounds))
    return roots, phi_coprime

roots,phi = roots_of_unity(e, N-1, N)
d = pow(e, -1,phi)
a = pow(c,d,N)
for root in roots:
    flag = long_to_bytes((root*a) % N)
    if b'flagformat' in flag:
        print(flag)             # THINE FLAG

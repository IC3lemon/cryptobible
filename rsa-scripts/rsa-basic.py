from sympy import *
from Crypto.Util.number import *

#  ----------rsa when p,q,c,e are available----------

#  Thine must have sympy and pycryptodome modules installed for this to worketh.


e = 65537
ct = b'encoded'  # thine ciphertext in bytes
c = bytes_to_long(cb) # thine ciphertext in long
p = 6969 # thy prime p
q = 6969 # thy prime q

N = p*q
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,N)

THINE_MESSAGE = long_to_bytes(m) # ----THINE MESSAGE HAST BEEN FOUND-----

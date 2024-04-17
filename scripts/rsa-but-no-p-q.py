import sympy as sp
from Crypto.Util.number import *

#  ----------rsa when N,c,e are available & N IS NOT PRIME----------

#  Thine must have sympy and pycryptodome modules installed for this to worketh.


e = 65537
ct = b'encoded'  # thine ciphertext in bytes
c = bytes_to_long(cb) # thine ciphertext in long
N = 69696969696 # thine N which ist NOT PRIME

factors = factorint(n)
p, q = factors.keys() # we FINDETH THINE PRIMESSSSS

phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,N)

THINE_MESSAGE = long_to_bytes(m) # ----THINE MESSAGE HAST BEEN FOUND-----

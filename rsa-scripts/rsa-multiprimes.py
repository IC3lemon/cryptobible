from sympy import *
from Crypto.Util.number import *

#  ----------rsa when thine has lot's of p's and q's----------

#  Thine must have sympy and pycryptodome modules installed for this to worketh.


e = 65537
ct = b'encoded'  # thine ciphertext in bytes
c = bytes_to_long(cb) # thine ciphertext in long
p = [696969, 696996, 69969696, 69969696, 9696969, 6969969, 69696996, 69969696, 696996, 69969696, 69969696, 9696969, 6969969, 69696996, 69969696] # THINE PRIMES

phi=1
for i in p:
    phi *= (i-1)

N =1
for i in p:
    N *= i
  
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,N)

THINE_MESSAGE = long_to_bytes(m) # ----THINE MESSAGE HAST BEEN FOUND-----

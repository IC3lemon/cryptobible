from Crypto.Util.number import *
from sympy import *
from sympy.ntheory.modular import crt

#  ----------rsa when multiple ciphertexts available i.e. CRT----------

#  Thine must have sympy and pycryptodome modules installed for this to worketh.


e = 65537

Ns = [69999699696996996996996969, 6969996999696969969999699696, ... ] # THINE N's
Cs = [696996969696996969, 69969696996996, 69969699696969969699, 69969699699696996, ... ] # THINE Ciphertext's


for n,c in zip(ns,cs):
    factors = factor(n)
    p = int(factors[0][0])
    q = int(factors[1][0])
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    m = pow(c,d,n)
    messages.append(m)
    modules.append(n)

flag = crt(messages,modules)[0]

THINE_MESSAGE = long_to_bytes(flag) # ----THINE MESSAGE HAST BEEN FOUND-----

from sympy import *
from Crypto.Util.number import *

#  ----------rsa when c,e,d are available, and size of primes known(assuming 128)----------

#  Thine must have sympy and pycryptodome modules installed for this to worketh.

e = 65537
ct = b'encoded'  # thine ciphertext in bytes
c = bytes_to_long(cb) # thine ciphertext in long

def countTotalBits(num):
     B_len = num.bit_length()
     return B_len 

# e*d = 1 mod (p-1)*(q-1)
# i.e.     e*d - 1 = k*(p-1)*(q-1)
# (p-1) and (q-1) would be 128 bits because p, q 128 bits

myboi = e*d - 1    

def factor3(myboi):
    divs = sp.divisors(myboi)
    all_128_bit_factors = []
  
    print(divs)
    for i in divs:
        if countTotalBits(i) == 128:
            all_128_bit_factors.append(i)

    for x in the128bois:
        for y in all_128_bit_factors:
            if myboi%(x*y) == 0:
                if sp.isprime(x+1) and sp.isprime(y+1):
                    p = x+1
                    q = y+1
                    break
            
N = p*q
phi = (p-1)*(q-1)
m = pow(c,d,N)

THINE_MESSAGE = long_to_bytes(m) # ----THINE MESSAGE HAST BEEN FOUND-----

from sage.all import *
from Crypto.Util.number import *

n = <modulus>
e = 3
c = <ciphertext>
padding = <padding>

R = PolynomialRing(Zmod(n), 'x')
x = R.gen()

# for some flag length 26, flag format "flag{}" and padding length 10
m = bytes_to_long(b'flag{' + b'\x00'*20 + b'}'+ padding)
f = (x*256**(len(padding)+1) + m)**3 - c (mod n)
roots = f.small_roots(X=256**20, beta=0.5)

print(long_to_bytes(int(roots[0])))

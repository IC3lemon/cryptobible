from sage.all import *
from Crypto.Util.number import *

# also demonstrated at sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots
# knowing upper bits of p / q can help in factoring n faster
# say _p = upper 824 bits of a 1024 bit p
# then p = _p << 200 + x
# where x is lower 200 bits of p

# to find x, given n, we can create a function
# f(x) = x + _p << 200 (mod p || q)
# roots of above function are satisfied only when rhs is p (mod p || q) i.e. 0
# thus roots of this equation yield lower 200 bits of p

_p = <upper '1024 - n' bits, for a 1024 bit prime>
N = <given N>
R = PolynomialRing(Zmod(N), 'x')
x = R.gen()

f = x + _p*2**n
lsb = (f.monic().small_roots(X=2**n, beta=0.4))[0]
p = int( lsb + _p*2**n ) # succesfully got p
q = N // p # successfully factored p, q
# make sure to have bounds set and an accurate beta, and the fact that the size of the missing root is correctly adjusted acc to degree(which is 1 in this case ig)

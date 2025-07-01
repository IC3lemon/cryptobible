from sage.all import *
from Crypto.Util.number import *

n = # modulus
R = PolynomialRing(Zmod(n))
f = # function to find small roots to
UB = # upper bounds for the unkown

root = f.small_roots(X=UB, beta=0.5)[0]
# make upper bound closest to the unkown, and make beta smaller in case of higher degree of f

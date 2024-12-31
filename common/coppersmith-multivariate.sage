from Crypto.Util.number import *
from sage.all import *

load("~/coppersmith.sage") # https://github.com/defund/coppersmith 

# example for bivariate func, can do the same for multivariate
bounds = ( ) # tuple containing upper bounds for each variable
n = # modulus
P.<x, y> = PolynomialRing(Zmod(n))
f = # function in x, y, whose roots to find
X, Y = small_roots(f, bounds)[0]

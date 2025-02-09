from Crypto.Util.number import *
from gmpy2 import iroot

def nth_root(a, n, p):
  """Computes nth root of a mod p"""
        g = GCD(n, p-1)
        e_prime = n // g
        t = (p - 1) // g
        d_prime = inverse(e_prime, t)
        X = pow(a, d_prime, p)
        root, exact = iroot(X, g)
        if exact:
            return root
        else:
            print("NO ROOTS")
            return None

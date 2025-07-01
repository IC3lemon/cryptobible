from sage.all import *

def nth_root(a, n, p): 
    return GF(p)(a).nth_root(n)

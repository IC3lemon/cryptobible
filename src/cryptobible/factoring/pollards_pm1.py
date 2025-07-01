from sage.all import *

def pollards_pm1(n, B=10^6):
    """
    factors n, given n has a prime factor p such that p - 1 is smooth
    Args :
        n : number to factor
        B : smoothness factor for n, largest prime that can appear in the factorization of p-1

    Returns : 
        d : a non-trivial factor of n
    """
    a = 2
    for p in range(2, B + 1):
        a = power_mod(a, p, n)  
        d = gcd(a - 1, n)
        if d > 1 and d < n:
            return d
    return None

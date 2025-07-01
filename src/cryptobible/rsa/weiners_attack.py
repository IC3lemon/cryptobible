from math import *
# from sage.all import *

def cont_fracs(x,y):
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients

def contfrac_to_rational (frac):
    if len(frac) == 0: return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac) - 1, -1): num, denom = frac[_] * num + denom, num
    return (num, denom)

def convergents(frac):
    convs = []
    for i in range(len(frac)): convs.append(contfrac_to_rational(frac[0 : i]))
    return convs
  
def weiners_attack(n : int, e : int) -> int:
    """
    Attack recovers private exponent d, and revolves around the fact that ed = 1 (mod phi)
    for huge e, if 1/e < 1/3 * fourth root of N.  d can be efficiently recovered.

    refer to github.com/IC3lemon/cryptobible/tree/main/RSA#weiners-attack 
    for further details on atatck's working

    Args:
        n : modulus
        e : public exponent

    Returns:
        d : private exponent

    perform pow(c, d, n) to recover plaintext
    """
    frac = cont_fracs(e, n)
    cgts = convergents(frac)
    
    for (k, d) in cgts:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if x*x - s*x + n = 0 has integer roots
            D = s * s - 4 * n
            if D >= 0:
                sq = sqrt(D)
                if sq * sq == D and (s + sq) % 2 == 0: 
                    return d



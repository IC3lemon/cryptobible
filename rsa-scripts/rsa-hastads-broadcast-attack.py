from Crypto.Util.number import *
import gmpy2
from functools import reduce

def chinese_remainder_theorem(items):
    N = reduce(lambda x, y: x * y, (item[1] for item in items))
    result = sum((N // item[1]) * gmpy2.invert(N // item[1], item[1]) * item[0] for item in items) % N
    return result

def hastads_broadcast_attack(ciphertexts, moduli, e):
    assert len(ciphertexts) == len(moduli), "The number of ciphertexts and moduli must be equal."
    assert len(ciphertexts) >= e, "The number of ciphertexts must be at least as large as the exponent."
    crt_result = chinese_remainder_theorem(list(zip(ciphertexts, moduli)))
    plaintext = gmpy2.iroot(crt_result, e)[0]
    return int(plaintext)


Ns = [N1, N2 ...] # thine Ns
Cs = [C1, C2 ...] # thins Cs

e = 696969 # thine e

flag = long_to_bytes(hastads_broadcast_attack(Ns, Cs, e))
print(flag.decode()) # flag

from Crypto.Util.number import *
import gmpy2
from functools import reduce

def chinese_remainder_theorem(items):
    N = reduce(lambda x, y: x * y, (item[1] for item in items))
    result = sum((N // item[1]) * gmpy2.invert(N // item[1], item[1]) * item[0] for item in items) % N
    return result

def hastad_broadcast_attack(ciphertexts : list, moduli : list, e : int) -> int:
    """
    Attack to be used when SAME MESSAGE is encrypted E times, and we have been provided corresponding moduli and ciphertexts
    no moduli should share factors, otherwise this attack fails due to crt not working in that case
    
    Args:
        ciphertexts : list of ciphertext integers
        moduli      : list of integer moduli corresponding to the ciphertext in that index
        e           : public exponent
    """
    assert e == len(moduli) == len(ciphertexts), "The amount of ciphertexts should be equal to e."
    for i in range(len(moduli)):
        for j in range(len(ciphertexts)):
            if i != j and gcd(moduli[i], moduli[j]) != 1:
                raise ValueError(f"Modulus {i} and {j} share factors, Hastad's attack is impossible.")
            
    crt_result = chinese_remainder_theorem(list(zip(ciphertexts, moduli)))
    plaintext = int(gmpy2.iroot(crt_result, e)[0])

    return plaintext

if __name__ == "__main__":
    Ns = [N1, N2 ...] # moduli
    Cs = [c1, c2, ...] # respective cipertexts
    
    flag = long_to_bytes(hastads_broadcast_attack(Cs, Ns, e))
    print(f"flag : {flag}") 

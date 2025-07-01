from sage.all import *
from Crypto.Util.number import getPrime, bytes_to_long




def hastad_broadcast_attack(ciphertexts: list, moduli: list, e: int) -> int:
    """
    Hastad's Broadcast Attack: Recovers the plaintext when the same message is
    encrypted with the same low exponent e and different coprime moduli.

    Args:
        ciphertexts : list of ciphertext integers
        moduli      : list of modulus integers (must be pairwise coprime)
        e           : low public exponent (e.g., 3)

    Returns:
        The recovered plaintext as an integer.
    """
    assert e == len(ciphertexts) == len(moduli), "Number of ciphertexts and moduli must be equal to e."

    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError(f"Moduli {i} and {j} are not coprime.")

    m_exp = crt(ciphertexts, moduli)

    m, exact = Integer(m_exp).nth_root(e, truncate_mode=True)
    if not exact:
        raise ValueError("e-th root not exact — attack failed (message too large?)")

    return int(m)

def test():
    e = 3
    m = b"flag{hastads_attack}"
    m_int = bytes_to_long(m)

    n_list = [getPrime(512) * getPrime(512) for _ in range(e)]
    c_list = [pow(m_int, e, n) for n in n_list]

    recovered = hastad_broadcast_attack(c_list, n_list, e)

    assert m == bytes.fromhex(hex(recovered)[2:])
    
if __name__ == "__main__":
    test()
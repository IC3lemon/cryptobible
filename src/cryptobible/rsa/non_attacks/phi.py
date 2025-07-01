def phi(factors: list) -> int:
    """
    recovers phi, given unique prime factorisation of n
    Example : for an N = p*p*q*r
    ϕ(n) = phi([p,p,q,r])

    Args:
        factors : factors of the number u are finding phi for

    ϕ(n) where n = p*q*r -> (p-1)*(q-1)*(r-1)
    ϕ(n) where n = p**k -> ((p**k)-(p**(k-1)))

    """
    from collections import Counter
    counts = Counter(factors)
    
    result = 1
    
    for element, count in counts.items():
        if count == 1:
            result *= (element - 1)
        else:
            result *= (element**count - element**(count - 1))
    
    return result

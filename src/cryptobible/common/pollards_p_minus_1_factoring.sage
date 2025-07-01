def pollards(n, B=10^6):
    a = 2
    for p in range(2, B + 1):
        a = power_mod(a, p, n)  
        d = gcd(a - 1, n)
        if d > 1 and d < n:
            return d
    return None

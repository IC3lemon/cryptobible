from sage.all import *

def fermat_factorisation(N):
    """
    Given N such that N = (a+b)*(a-b) factor N to give it's factors p and q
    Args:
        N: a number of the form (a+b)*(a-b)
    Returns:
        p: factor of N
        q: factor of N

    """
    a = ceil(sqrt(N))
    while True:
        b_sq = a**2 - N 
        if b_sq < 0:
            a += 1
            continue
        b = floor(sqrt(b_sq))
        if b_sq == b**2:
            p , q = a + b, a - b
            return p,q        
        a += 1

def test():
    while True:
        a,b = randint(0,1000),randint(0,1000)
        if b > a:
            a,b = b,a
        if is_prime(a+b) and is_prime(a-b):
            break
    if b > a:
        a,b = b,a
    N = a**2 - b**2
    assert(fermat_factorisation(N) == (a+b,a-b))

if __name__ == "__main__":
    test()

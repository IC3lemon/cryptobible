# DO NOT import this file into __init__.py as sage already has Elliptic Curves built-in

from sage.all import inverse_mod

def point_addition(P, Q, a, p):
    O = (None, None) 
    if P == O:
        return Q
    if Q == O:
        return P
    
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 == (-y2) % p):
        return O

    if P != Q:
        l = ((y2 - y1) % p) * inverse_mod(x2 - x1, p) % p
    else:
        l = ((3*x1*x1 + a) % p) * inverse_mod(2*y1, p) % p
    x3 = (l**2 - x1 - x2) % p 
    y3 = (l*(x1 - x3) - y1) % p
    return (x3, y3)

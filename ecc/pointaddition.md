![image](https://github.com/user-attachments/assets/571c58a5-e09e-452a-8939-de67cad6557b)

```py
from Crypto.Util.number import *

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
        l = ((y2 - y1) % p) * inverse(x2 - x1, p) % p
    else:
        l = ((3*x1*x1 + a) % p) * inverse(2*y1, p) % p
    x3 = (l**2 - x1 - x2) % p 
    y3 = (l*(x1 - x3) - y1) % p
    return (x3, y3)
```

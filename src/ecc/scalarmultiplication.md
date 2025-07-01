![image](https://github.com/user-attachments/assets/d3c4cc2a-408e-49e9-9bc5-c38b2ca9936c)

```py
from Crypto.Util.number import *
from pointaddition import *

def scalar_multiplication(P, n, a=497, p=9739):
    O = (None, None)
    Q = P
    R = O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q, a, p)
        Q = point_addition(Q, Q, a, p)  
        n = n // 2
    return R
```

# `Mod math`

## Quadratic Residue 

`a**2 % p = x` \
here, `p` is some prime, \
**`x`** is ur **`quadratic residue`** \
`a` is `sqrt of x` \
**[ not the normal sqrt, weird mod math sqrt ]**

basic cringe script to check if a number is a quad residue :
```python
from Crypto.Util.number import *

p = 29
num = 6
yes = 0
for a in range(1,p):
  if pow(a,2,p) == int:
    residue = int
    print(f"{num} is a quadratic residue.")
    print(f"square root : {a}")
    yes = 1
    break
if yes = 0:
  print("not a quad residue.")
```

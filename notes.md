## `Quadratic Residue`



`a**2 % p = x` \
here, `p` is some prime, \
**`x`** is ur **`quadratic residue`** \
`a` is `sqrt of x` \
**[ not the normal sqrt, weird mod math sqrt ]**

basic cringe bruteforce script to check if a number is a quad residue :
(would work only for small p)
```python
from Crypto.Util.number import *

p = 29
num = 6
yes = 0
for a in range(1,p):
  if pow(a,2,p) == num:
    residue = num
    print(f"{num} is a quadratic residue.")
    print(f"square root : {a}")
    yes = 1
    break
if yes = 0:
  print("not a quad residue.")
```

```
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue
```

## `Legendre Symbol`



Legendre's Symbol: `(a / p) ≡ a(p-1)/2 mod p` obeys:
```
(a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
(a / p) = -1 if a is a quadratic non-residue mod p
(a / p) = 0 if a ≡ 0 mod p
```
Which means given any integer `a`, calculating `pow(a,(p-1)//2,p)` is enough to determine if `a` is a quadratic residue. 


dam so technically, say u got a number `A = a**num % p` \
we can find if num is odd or even. \
if A is quadratic residue i.e. even, `legendre(A) = 1` \
if A is not quadratic residue i.e. odd, `legendre(A) = -1`

python implementation : 
```python
from sympy import legendre_symbol

p = BIG_ASS_PRIME
A = SOME_BIG_AAH_INT

if legendre_symbol(A,p) == 1:
    print("yes quad residue")
else:
    print("no quad residue")
```
```python
def legendre_symbol(a,p):
    symbol = pow(a,(p-1)//2,p)
    if symbol == 1:
        print("yes quad residue")
        return True
    else:
        print("no quad residue")
        return False
```

## `Euler's Criterion` 



if `a` is a quadratic residue \
`a**((p-1)//2)) ≡ 1 mod p` 

so say u wanna find sqrt `x` for a quadratic residue `a`. \
`x**2 ≡ a mod p` \
so multiply a on both sides on Euler's criterion, u get : \
`a**((p+1)//2) ≡ a mod p` \
=> `[a**((p+1)//4)] **2 ≡ a mod p` \
now this looking like `x**2 ≡ a mod p`

so therfore u can calculate yo roots with \
**` x = a**((p+1)//4) `**

but for this to work, `(p+1)/4` has to be not decimal. \
Thus it works only in the case of `p+1 ≡ 0 mod 4` || `p ≡ -1 mod 4` || `p ≡ 3 mod 4`

```python
from sympy import legendre_symbol

num = THE_QUAD_RES_WHOS_SQRT_WE_NEED
p = BIG_ASS_PRIME

assert legendre_symbol(num,p) == 1
assert p % 4 == 3
exp = (p+1)//4
sqt = pow(x,exp,p)
print(f"{sqt} is the square root")
```

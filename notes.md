# `Quadratic Residue`



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
if yes == 0:
  print("not a quad residue.")
```

```
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue
```

# `Legendre Symbol`



Legendre's Symbol: `(a / p) ≡ a(p-1)/2 mod p` obeys:
```
(a / p) = 1 if a is a quadratic residue and a ≢0 mod p
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

# `Euler's Criterion` 



if `a` is a quadratic residue \
`a**((p-1)//2)) ≡ 1 mod p` 

so say u wanna find sqrt `x` for a quadratic residue `a`. \
`x**2 ≡ a mod p` \
so multiply a on both sides on Euler's criterion, u get : \
`a**((p+1)//2) *a ≡ 1 *a  mod p` \
=> `[a**((p+1)//4)] **2 ≡ a mod p` \
now this looking like `x**2 ≡ a mod p`

so therfore u can calculate yo roots with \
**` x = a**((p+1)//4) `**

but for this to work, `(p+1)/4` has to be not decimal. \
**Thus it works only in the case of `p+1 ≡ 0 mod 4` || `p ≡ -1 mod 4` || `p ≡ 3 mod 4`**

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
All primes that aren't 2 are of the form 
```
p ≡ 1 mod4 or 
p ≡ 3 mod4
```

for `p ≡ 3 mod4` u can use eulers criterion [ OR tonelli-shanks ]\
for `p ≡ 1 mod4` u gotta use tonelli-shanks 


# `Tonelli-Shanks`


![image](https://github.com/user-attachments/assets/a9a3387d-c0e0-4cbf-be0f-dbce63ec9d65) \
![image](https://github.com/user-attachments/assets/6bf32abc-67d8-421c-ae0d-6ec6e39d3b51)


steps to find modular square root of A using shank Tonelli’s algorithm :

1. Check if `A` is quadratic residue
2. write `p-1` in terms of `s * (2**e)`
3. find smallest `q` such that `q **((p – 1) / 2)  % p = p-1 `
4. set `x = A**((s+1)/2) % p` \
   set `b = A**s % p` \
   set `g = q**s % p` \
   set `r = e`
5. Now loop till `m=0` or `b=1` for below process
```
Find least integer m such that b^(2^m) = 1(mod p)  and  0 <= m <= r – 1 
   If m = 0, then we found correct answer and return x as result
   Else update x, b, g, r as below
       x = x * g ^ (2 ^ (r – m - 1))
       b = b * g ^(2 ^ (r - m))
       g = g ^ (2 ^ (r - m))
       r = m
```
 if m becomes 0 or b becomes 1, we terminate and print the result.  \
 This loop guarantees to terminate because value of m is decreased each time after updation.

Implementation : 
```python

a = BIG_NUM
p = BIG_NUM

# x**2 % p = a % p | need to find x

# reference : https://www.geeksforgeeks.org/find-square-root-modulo-p-set-2-shanks-tonelli-algorithm/

from sympy import legendre_symbol

def tonelli(a : int,p : int) -> int: 

    if legendre_symbol(a,p) == 1:       # check if a IS a quadratic residue
        s = p - 1
        e = 0
        while s % 2 == 0:
            s = s // 2
            e += 1                      # compute s,e such that  p-1 = s * (2**e)
        
        q=2
        while True:                     # find smallest q such that q **((p – 1) / 2)  % p = p-1 
            if pow(q, (p-1)//2, p) == p-1:
                break
            else:
                q += 1

        x = pow(a,(s+1)//2,p)
        b = pow(a,s,p)
        g = pow(q,s,p)
        r = e

        while True:  
            m = 0                       # find least integer m such that b^(2^m) = 1(mod p)  and  0 <= m <= r – 1 
            while m < r:                        
                if pow(b,pow(2,m),p) == 1:  
                    break
                else:
                    m += 1
            
            if m == 0:
                return x                # got it
            else:
                x = (x * pow(g ,pow(2,r-m-1), p))  % p
                b = b * pow(g,pow(2,r-m), p)
                g = pow(g,pow(2,r-m), p)
                r = m
            
            if b == 1:
                return x

print(tonelli(a,p))
```

# `Chinese Remainder Theorem`

if u have a bunch of congruences such that : 
```
x ≡ a1 mod n1
x ≡ a2 mod n2
x ≡ a3 mod n3
```
there exists `a` such that : ` x ≡ a mod N ` \
where `N = n1 * n2 * n3`

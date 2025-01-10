# `Euler's theorem + why RSA works`

This also covers why `ed = 1 (mod phi(n))` works in RSA \
In RSA encryption / decryption : 
```
c = m**e (mod n)
m = c**d (mod n)

i.e.

m = (m**e)**d (mod n)
m = m**(ed)   (mod n)
m**(ed) = m   (mod n)
```
now Euler's theorem states \
for any `m` coprime to `n` 
```py
m**(phi(n)) = 1 (mod n)
```
thus, if `ed = 1 (mod phi)` \
```
   m**(ed)                 (mod n)
=> m**(1 + k*phi)          (mod n)
=> m * (m**(k*phi))        (mod n)
=> m * 1                   (mod n)
=> m                       (mod n)
```
ensures a private key that 100% works.

# `Fermat's Little Theorem`

<p><b>Fermat's little theorem</b> states that if <span class="texhtml mvar" style="font-style:italic;">p</span> is a prime number</a>, then for any integer</a> <span class="texhtml mvar" style="font-style:italic;">a</span>, the number <b><span class="texhtml"><i>a</i><sup><i>p</i></sup> − <i>a</i></span></b> is an integer multiple of <span class="texhtml mvar" style="font-style:italic;"></b>p</span>. 
</p>

anything of the form \
`(a**p) - a` is divisible by `p` 
> given that : \
> `a is an integer` \
> `p is prime`



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

implementation : 
```python
from sympy.ntheory.modular import crt

moduli = [n1, n2, n3]
residues = [a1, a2, a3]
x = crt(moduli, residues)[0]
```

# `Euler's phi function`

the Euler phi function, written `ϕ(n)`, for positive integers `n`. \
`ϕ(n)` is the number of non-negative integers less than `n` that are relatively prime to `n`.

***

**some basic properties of phi :**

## `phi(1) = 1` 

## if `p` is a prime,
![image](https://github.com/user-attachments/assets/b4d18546-fdb0-4dbd-afa6-5615916d845b) \
because 1, 2 ... p-1 are relatively prime to p

## if `p` is a prime and `a` is a positive integer 
![image](https://github.com/user-attachments/assets/448d22f5-bded-48c2-b9aa-53f50c7f3963)

## if `a` and `b` are relatively prime then
![image](https://github.com/user-attachments/assets/bcc5f54f-7b21-4609-bdfa-6f3943daf257)

## if `n` is an integer with prime factors, `p1`, `p2`, ... `pn`
![image](https://github.com/user-attachments/assets/45d46aa4-0a90-43b5-ac8e-aaf412e568c3)

# `Gram Schmidt`

Given a basis for a vector space, `V = {v1, v2, v3, v4 ... vn}` \
You can compute an orthogonal basis `u1, u2, u3, ... un ∈ V` \
![image](https://github.com/user-attachments/assets/7edbfdaf-0cda-40d4-9bc5-e7cf75040cf3)

```python

def dot(a: list, b: list) -> float:
    # Ensure both lists have the same length by padding with zeros
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    elif len(b) < len(a):
        b += [0] * (len(a) - len(b))
    
    dot_product = sum(x * y for x, y in zip(a, b))
    return dot_product

def scalar(a: float, b: list) -> list:
    return [a * i for i in b]

def sub(a: list, b: list) -> list:
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    elif len(b) < len(a):
        b += [0] * (len(a) - len(b))
    return [A - B for A, B in zip(a, b)]

def gram_schmidt(V: list) -> list:
    # Initialize orthogonal basis U
    U = [None] * len(V)
    U[0] = V[0]  # First vector remains the same
    
    for i in range(1, len(V)):
        # Start with the current vector
        U[i] = V[i]
        for j in range(i):
            # Project V[i] onto U[j] and subtract the projection from U[i]
            u_ij = dot(V[i], U[j]) / dot(U[j], U[j])
            U[i] = sub(U[i], scalar(u_ij, U[j]))
    
    return U

V = [(4, 1, 3, -1), (2, 1, -3, 4), (1, 0, -2, 7), (6, 2, 9, -5)] # whatever ur vector basis is
U = gram_schmidt(V)

print("Orthogonal basis:", U)
```
# `Gaussian Lattice Reduction`

reduces 2d lattices, given a bad basis
```python
def mag(vector):
    return vector[0]**2 + vector[1]**2

def dot(a, b):
    # Ensure both lists have the same length by padding with zeros
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    elif len(b) < len(a):
        b += [0] * (len(a) - len(b))
    
    dot_product = sum(x * y for x, y in zip(a, b))
    return dot_product

def scalar(a: float, b: list) -> list:
    return [a * i for i in b]

def sub(a: list, b: list) -> list:
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    elif len(b) < len(a):
        b += [0] * (len(a) - len(b))
    return [A - B for A, B in zip(a, b)]

def Gaussian_Lattice_Reduction(basis):
    v1 = basis[0]
    v2 = basis[1]
    while True:
        if mag(v1) > mag(v2):
            v1, v2 = v2, v1
        m = int(dot(v1,v2) / dot(v1, v1))
        if m == 0:
            return [v1, v2]
        v2 = sub(v2 ,scalar(m,v1))

good_basis = Gaussian_Lattice_Reduction(bad_basis)
```
sagemath implementation :
```sage
def Gaussian_Lattice_Reduction(basis):
    v1 = basis[0]
    v2 = basis[1]
    if basis[1] > basis[0]:
        v1 = basis[1]
        v2 = basis[0]
    while True:
        if v1.norm() < v2.norm():
            v1, v2 = v2, v1 # obviously should swap if this is the case
        p = round(v1.dot_product(v2)/v2.dot_product(v2)) # projecting the taller vector onto the shorter & round to the spanned lattice
        if p == 0:
            break
        v1 -= p*v2 # reduce the taller vector
    
    return [v1, v2]
```
*** 
# SIDE NOTES :
1. `bytes_to_long(b'crypto{\x00\x00\x00}') + bytes_to_long(b'\x00\x00\x00\x00\x00\x00\x00abc\x00') = bytes_to_long(b'crypto{abc}')`
2. `a % (a-x) = x`
3. `-a % x = x - (a % x)` 

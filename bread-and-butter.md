# `Basic conversions`

```python
from Crypto.Util.number import *

# int to bytes, byte to int
a = b"blahblah"
b = bytes_to_long(a)
c = long_to_bytes(b)

# bytes to hex, hex to bytes
a = "deadbeef"
b = bytes.fromhex(a)
c = hex(bytes_to_long(b))

# base64, 58 whatever
import base64
...
...
import base58

a = "d293IHUgZGVjb2RlZCB0aGlzLiBjcmF6eS4gdXIgc28gdGFsZW50ZWQuIHNvIHNtYXJ0IA=="
b = base64.b64decode(a).decode()
c = base64.b64encode(a.encode())

# individual byte list to bytestring ?
a = [101, 234, 255, 10, 11, 12]
b = bytearray(a)
```
# `Basic factoring`

> ### factordb

goated. \
alternatively visit <a href=https://factordb.com/>the site.</a> but scripting encouraged. \
use `pip install factordb-pycli` for the module.
```python
from factordb.factordb import FactorDB

N = # number to be factored
f = FactorDB(N)
f.connect()
primes = f.get_factor_list()
```

> ### sympy

less goated. Use for smaller numbers ig. 
```python
from sympy import *

N = # number to be factored
factors = factorint(N).keys()
```

***

other algorithms for factoring may include : 
- `lenstras ecm`
- `pollard's p-1`
- `Quadratic Sieve`
  
# `solving a set of equations`

> ### sympy
```python
from sympy import *  # pip install sympy

x,y,z = symbols('x y z')
eq1 = Eq( # LHS, # RHS )
eq2 = Eq( # LHS, # RHS )
eq3 = Eq( # LHS, # RHS )

# for n unknowns, n equations only.
```

> ### z3
```python
from z3 import *   # pip install z3-solver

solver = Solver()
x = Int('x')
y = Int('y')
z = Int('z')

solver.add( # first equation in the form : LHS == RHS )
solver.add( # second equation in the form : LHS == RHS )
solver.add( # third equation in the form : LHS == RHS )

# can also add conditions in z3 such that :
solver.add( x > y )
solver.add( y > z )
```
learn z3 -> https://github.com/ViRb3/z3-python-ctf

# `vector basics`

## linearly independent vectors 
consider a set of vectors
```
V = {v1, v2, v3 ... vn}
```
if these vectors are `linearly independent` then
```
v1a1 + v2a2 + ... + vnan = 0

only if
a1=a2=...=an=0
```
![image](https://github.com/user-attachments/assets/938bb401-adb8-4229-9e42-6a61e29ea99a)

## BASIS
A set of linearly independent vectors `V = {v1, v2 ... vn}` \
can be called a basis if you can define a vector `w = v1a1 + v2a2 + ... + vnan` and `w ∈ V` \

![image](https://github.com/user-attachments/assets/a2510d29-e66f-4181-96d7-e3d30017b435)

- `The number of elements in the basis = the dimension of the vector space.`
## `size of a vector  ∣∣v∣∣`
`literally magnitude of a vector`

## `orthogonal basis`
for a vector basis `V = {v1, v2 ... vn}` \
if the dot product between any two vectors is `0` the basis is orthogonal \
![image](https://github.com/user-attachments/assets/6379c0a2-7565-46b4-bf42-bbce47f1f707)

## `orthonormal basis`
for a vector basis `V = {v1, v2 ... vn}` \
if a basis is orthogonal AND for every `vi` in `V` \
`|vi| = 1`

# `lattice`
literally just watch this -> <a href="https://www.youtube.com/watch?v=FcgN_ijcU6g">`https://www.youtube.com/watch?v=FcgN_ijcU6g`</a> \
the normal coordinate system as a lattice -> basis of `[[1,0,0],[0,1,0],[0,0,1]]`


# `cheating basically`

`cyber chef` -  https://gchq.github.io/CyberChef/ \
`dcode` -  https://www.dcode.fr/en \
`enigma` - https://cryptii.com/pipes/enigma-machine \
`morse` - https://morsecode.world/international/translator.html \
`citrix ctx1` - https://asecuritysite.com/cipher/citrix

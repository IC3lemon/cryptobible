
- [`conversions`](https://github.com/IC3lemon/cryptobible/tree/main/bread-and-butter.md#basic-conversions)
- [`factoring`](https://github.com/IC3lemon/cryptobible/tree/main/bread-and-butter.md#basic-factoring)
- [`solving equations`](https://github.com/IC3lemon/cryptobible/tree/main/bread-and-butter.md#solving-a-set-of-equations)
- [`cheating`](https://github.com/IC3lemon/cryptobible/tree/main/bread-and-butter.md#cheating-basically)
  
***
# `Basic conversions`

> ## int to bytes, byte to int
```py
from Crypto.Util.number import *

a = b"blahblah"
b = bytes_to_long(a)
c = long_to_bytes(b)
```
> ## bytes to hex, hex to bytes
```py
from Crypto.Util.number import *

a = "deadbeef"
b = bytes.fromhex(a)
c = hex(bytes_to_long(b))
```
> ## base64, 58 whatever
```py
import base64

a = "d293IHUgZGVjb2RlZCB0aGlzLiBjcmF6eS4gdXIgc28gdGFsZW50ZWQuIHNvIHNtYXJ0IA=="
b = base64.b64decode(a).decode()
c = base64.b58decode(a).decode()
```
> ## individual byte list to bytestring ?
```py
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
> ### [ALPERTRON](https://www.alpertron.com.ar/ECM.HTM)
***

other algorithms for factoring may include : 
- `lenstras ecm`
- `pollard's p-1`
- `Quadratic Sieve`
 \
 // to be implemented and logged
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

# `cheating basically`

`cyber chef` -  https://gchq.github.io/CyberChef/ \
`dcode` -  https://www.dcode.fr/en \
`enigma` - https://cryptii.com/pipes/enigma-machine \
`morse` - https://morsecode.world/international/translator.html \
`citrix ctx1` - https://asecuritysite.com/cipher/citrix

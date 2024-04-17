
***
<br>

1. Thine must have pycryptodome and sympy modules installed for above scripts to work.
2. Thine must take note of the first commented sentence to know what thine art dealing with
3. Below described are the methods and knowledge of how above scriptures came into being
   
<br>

***

# RSA

```
the bread and butter. The unquestioned, undoubted goat.
You have ciphertexts which are encrypted via a public key (N,e),
and decrypted via a private key (d,e) which is kept secret.

The relations between them...
N = p * q     Where p and q are certain secret prime numbers
e = an exponent (usually 65537)
d = mod_inv(e, (p-1)*(q-1))

the ciphertext is constructed via : c = (m**e) % N
```
in a nutshell : 
![image](https://github.com/IC3lemon/cryptobible/assets/150153966/bc39b6b0-a9a4-405c-9f16-ad65a82a84e9)

<br>

The basic RSA script I cooked when I was but a young crypto hatchling > <a href="https://github.com/IC3lemon/cryptobible/blob/main/scripts/rsa-basic.py">`the salvation`</a>

<br>

special cases I encountered with RSA : 
  1. **N is a prime number** > <a href="https://github.com/IC3lemon/cryptobible/blob/main/scripts/rsa-N-is-prime.py">`the salvation`</a>
      > A concept called the roots of unity was applied to solve this case
<br>

  2. **Multiple ciphertexts** > <a href="https://github.com/IC3lemon/cryptobible/blob/main/scripts/rsa-CRT-multiple-ciphertexts.py">`the salvation`</a>
      > A concept called CRT i.e. Chinese Remainder Theorem applied
<br>

  3. **Multiple primes** > <a href="https://github.com/IC3lemon/cryptobible/blob/main/scripts/rsa-multiprimes.py">`the salvation`</a>
      > No specific concept, N is still the product of all the primes, phi is the product of all primes-1
<br>

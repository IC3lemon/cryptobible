# `RSA`

The undoubted unquestioned goat. \
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

## Attacks logged here 
- [`common modulus attack`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-common-modulus-attack.py)
- [`hastad's broadcast attack`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-hastads-broadcast-attack.py)
- [`wiener's attack`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-weiners-attack.py)
- [`attacks on phi`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-attacks-on-phi.py)
- [`coppersmith's attack for random pads`](https://github.com/IC3lemon/cryptobible/blob/main/rsa/rsa-coppersmiths-attack.py)

***
# common-modulus-attack

### `SITUATION :`
when same message `m` has been encrypted twice. \
using the same `n`, but different `e` such that : 
```
c1 = m ** e1   % n
c2 = m ** e2   % n
```
m can be extracted

> [!NOTE]
> `e1` `e2` must be coprime for this attack to work.

### `how it works :`

since `e1`, `e2` are coprime
```
gcd(e1, e2) = 1
```

now we know that according to `extended euclidean algorithm` \
for the gcd of any two numbers `x` and `y`, \
there exists `a`, `b` such that
```
ax + by = gcd(x, y)
```
this a, b can be calculated using `egcd`

similarly for e1, e2
```
a*e1 + b*e2 = 1      ----- 1
```

now our message m 
```
m = m**1 % n
```
replacing 1 with eqn 1
```
m = m**(ae1 + be2)  % n
m = ( m**ae1 ) * ( m**be2 ) % n
m = ( c1**a  ) * ( c2**b )  % n 
```
we can find a, b thus decrypted.

***
# hastad-broadcast-attack

### `SITUATION :`
when the same message `m` \
has been encrypted `e` times \
with a corresponding `N` `C` for each encrypted broadcast. 

m can be extracted in this case.

> [!NOTE]
> All the `N`'s need to be coprime, none can share factors, otherwise this attack fails

### `how it works :`

you essentially have
```
c1 = m ** e % n1
c2 = m ** e % n2
.
.
.
ck = m ** e % nk
```
we can rearrange this to form the congruences 
```
m**e = c1 % n1
m**e = c2 % n2
m**e = c3 % n3
.
.
.
m**e = ck % nk
```

crt can solve this system of congruences to give us the original value for `m**e` \
then just simply find the `e th` root of that value to get `m`
***
# Coppersmith's attack for random padding

### `SITUATION :`
when message `m` has been padded with some randomness `a` \
and public exponent e is a low number \
the padding, and the length of the flag also has to be known. 

> [!NOTE]
> `flag format`, `padding` and any information about the message encrypted must be added to the equation to reduce the size of the unkown.
> the bounds `X` must be equal to the number of bits of the unkown ur trying to find. (can be greater, but much larger bounds might not yield a solution)
> ```
> x < n**(1/e)
> beta > (1/e)
> ```
> both of the above must hold true

### `how it works :`

you essentially have an equation
```
c = (m + a)**3 (mod n)
f(m) = (m + a)**3 - c (mod n)
```
which you solve for m. Coppersmith does exactly that, it finds small roots for a polynomial. \
Which is why reducing the size of the unknown matters, because smaller the root is, better coppersmith's works on it.


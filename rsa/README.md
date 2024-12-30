# `RSA`

The undoubted unquestioned goat. \
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

## Attacks logged here 
- [`common modulus attack`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-common-modulus-attack.py)
- [`hastad's broadcast attack`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-hastads-broadcast-attack.py)
- [`wiener's attack`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-weiners-attack.py)
- [`attacks on phi`](https://github.com/IC3lemon/cryptobible/blob/main/rsa-scripts/rsa-attacks-on-phi.py)
- [`coppersmith's attack for random pads`]

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


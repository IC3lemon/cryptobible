#!/usr/bin/env python3

from Crypto.Util.number import *
from flag import flag

def man(n):
	B = bin(n)[2:]
	M = ''
	for b in B:
		if b == '0':
			M += '01'
		else:
			M += '11'
	return int(M, 2)

def keygen(nbit):
	while True:
		p = getPrime(nbit)
		r = man(p)
		B = bin(p)[2:] + '1' * nbit
		q = int(B, 2)
		if isPrime(q) and isPrime(r):
				return q, r

nbit = 256
p, q = keygen(nbit)
m = bytes_to_long(flag)
assert m < n
e, n = 1234567891, p * q
c = pow(m, e, n)

print(f'n = {n}')
print(f'c = {c}')
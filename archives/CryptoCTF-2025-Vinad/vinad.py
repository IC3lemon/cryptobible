#!/usr/bin/env python3

from Crypto.Util.number import *
from flag import flag

def parinad(n):
	return bin(n)[2:].count('1') % 2

def vinad(x, R):
	return int(''.join(str(parinad(x ^ r)) for r in R), 2)

def genkey(nbit):
	while True:
		R = [getRandomNBitInteger(nbit) for _ in range(nbit)]
		r = getRandomNBitInteger(nbit)
		p, q = vinad(r, R), getPrime(nbit)
		if isPrime(p):
			e = vinad(r + 0x10001, R)
			if GCD(e, (p - 1) * (q - 1)) == 1:
				return (e, R, p * q), (p, q)

def encrypt(message, pubkey):
	e, R, n = pubkey
	return pow(message + sum(R), e, n)

nbit = 512
pubkey, _ = genkey(nbit)
m = bytes_to_long(flag)
assert m < pubkey[2]
c = encrypt(m, pubkey)

print(f'R = {pubkey[1]}')
print(f'n = {pubkey[2]}')
print(f'c = {c}')
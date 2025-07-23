#!/usr/bin/env sage

from Crypto.Util.number import *
from flag import flag

def randpos(n):
	if randint(0, 1):
		return True, [(-(1 + (19*n - 14) % len(flag)), ord(flag[(63 * n - 40) % len(flag)]))]
	else:
		return False, [(randint(0, 313), (-1) ** randint(0, 1) * Rational(str(getPrime(32)) + '/' + str(getPrime(32))))]

c, n, DATA = 0, 0, []
while True:
	_b, _d = randpos(n)
	H = [d[0] for d in DATA]
	if _b:
		n += 1
		DATA += _d
	else:
		if _d[0][0] in H: continue
		else:
			DATA += _d
			c += 1
	if n >= len(flag): break

A = [DATA[_][0] for _ in range(len(DATA))]
poly = QQ['x'].lagrange_polynomial(DATA).dumps()
f = open('output.raw', 'wb')
f.write(poly)
f.close()
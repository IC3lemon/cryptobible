   1   │ import hashlib
   2   │ import itertools
   3   │ import os
   4   │ 
   5   │ def xor(key, data):
   6   │     return bytes([k ^ d for k, d in zip(itertools.cycle(key), data)]
       │ )
   7   │ 
   8   │ def encrypt(phrase, message, iters=1000):
   9   │     key = phrase.encode()
  10   │     for _ in range(iters):
  11   │         key = hashlib.md5(key).digest()
  12   │         message = xor(key, message)
  13   │     return message
  14   │ 
  15   │ print('Welcome to my encryption service!')
  16   │ print('Surely encrypting multiple times will make it more secure.')
  17   │ print('1. Encrypt message.')
  18   │ print('2. Encrypt (hex) message.')
  19   │ print('3. See encrypted flag!')
  20   │ 
  21   │ phrase = os.environ.get('FLAG', 'missing')
  22   │ 
  23   │ choice = input('Pick 1, 2, or 3 > ')
  24   │ if choice == '1':
  25   │     message = input('Your message > ').encode()
  26   │     encrypted = encrypt(phrase, message)
  27   │     print(encrypted.hex())
  28   │ if choice == '2':
  29   │     message = bytes.fromhex(input('Your message > '))
  30   │     encrypted = encrypt(phrase, message)
  31   │     print(encrypted.hex())
  32   │ elif choice == '3':
  33   │     print(encrypt(phrase, phrase.encode()).hex())
  34   │ else:
  35   │     print('Not sure what that means.')

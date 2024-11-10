# AES ECB ENCRYPTION ORACLE
"""
use this script for the scenario in which, 
u have an encryption oracle that attaches an extra block (probably the flag)

i.e. the encryption is something like :

ENCRYPT( USER INPUT + SECRET )

refer to this for more detail on the attack -> https://0awawa0.medium.com/break-me-downunder-ctf-2021-writeup-d2f4db2144b6
or refer to README.md under aes [TODO]
"""
from pwn import *
from Crypto.Util.number import *

r = remote('host', port)

found = bytearray(b'')

for x in range(16, -1, -1):
    payload = b'a'*x
    hex_payload = hex(bytes_to_long(payload))[2:]

    r.recvuntil(b'Enter plaintext (in hex): ')
    r.sendline(hex_payload.encode())
    recieved = r.recvline().decode().strip()
    yes = recieved[:16]
    for i in range(256):
        
        bhai = b'a'*x  + found + chr(i).encode()
        pls = hex(bytes_to_long(bhai))[2:]
        r.recvuntil(b'Enter plaintext (in hex): ')
        r.sendline(pls.encode())
        recieved = r.recvline().decode().strip()[:16]
        if(yes == recieved):
            print('secret found : ', chr(i))
            found.append(i)
            break
    print(f'[*] (iteration {x}/16) constructed : {found}')
    x -= 1

print(f"\n\nFLAG / SECRET : {found})

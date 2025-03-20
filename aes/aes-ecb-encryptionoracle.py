# AES ECB ENCRYPTION ORACLE
"""
use this script for the scenario in which, 
u have an encryption oracle that attaches an extra block (probably the flag)

i.e. the encryption is something like :

ENCRYPT( USER INPUT + SECRET )

refer to this for more detail on the attack -> https://0awawa0.medium.com/break-me-downunder-ctf-2021-writeup-d2f4db2144b6
or refer to README.md under aes [TODO]
"""
from Crypto.Util.number import *
from tqdm import tqdm
import requests
import string

def encrypt(plaintext):
    """oracle function that takes plaintext bytes returns ciphertext bytes"""
    ciphertext = 'received from server' # edit accordingly
    return bytes.fromhex(ciphertext)

nblocks = len(encrypt(b"\x00"*16)[16:]) // 16
charset = string.printable

flag = "" 
for i in range(nblocks):
    flag_block = ""
    target = encrypt(b"\x00"*16)[16*(i+1):16*(i+2)]
    for x in tqdm(range(15, -1, -1), leave=False):
        if i == 0:
            payload = b"\x00"*x
        else:
            payload = b"\x00"*(16 - len(flag_block)//2 - 1)

        if x == 0:
            recieved = target
        else:
            recieved = encrypt(payload)[16*i:16*(i+1)]
        for c in charset:
            if recieved == encrypt(payload+flag.encode()+c.encode())[16*i:16*(i+1)]:
                flag_block += c
                flag += c
                break
        if c == '}':
            break
    print(f"block {i+1} : {flag_block}")
print(f"\n{flag}")

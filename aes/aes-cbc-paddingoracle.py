from pwn import remote, xor
from binascii import hexlify, unhexlify

conn = remote('whatever', 696969)

ct = unhexlify("ciphertext hex")

assert len(ct) % 16 == 0

blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
pt = b''

def oracle(payload):
    conn.oraclelineafter(b'Please enter the ciphertext: ', payload)
    response = conn.recvline().strip()
    if b'No Error' in response:
        return True
    else: return False

def get_key_byte(ind, c0, c1, c2):
    for guess in range(256):
        modified_c1 = bytearray(c1)
        modified_c1[-ind] = guess
        payload = hexlify(c0 + bytes(modified_c1) + c2)
        if oracle(payload):
            print(f"ind: {ind}\t guess: {guess}")
            return guess
    return -1

def get_keystream(c0, c1, c2):
    keystream = bytearray(16)
    keystream[-1] = get_key_byte(1, c0, c1, c2) ^ 0x01 ^ c2[-1]
    for ind in range(2, 17):  
        c1 = bytearray(c1)
        for i in range(1, ind):
            c1[-i] = keystream[-i] ^ ind ^ c2[-i]
        c1 = bytes(c1)
        keystream[-ind] = get_key_byte(ind, c0, c1, c2) ^ ind ^ c2[-ind]
        print(f"ind: {ind}\t keystream: {bytes(keystream)}")
    return keystream

for i in range (0, len(blocks)-2):
    keystream = get_keystream(blocks[i], blocks[i+1], blocks[i+2])
    pt = pt + xor(keystream, blocks[i+1], blocks[i+2])
    print(pt)

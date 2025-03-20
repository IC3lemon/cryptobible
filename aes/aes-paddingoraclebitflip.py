from Crypto.Util.Padding import *
from pwn import *
from tqdm import *

def oracle(ciphertext):
    """sends ciphertext to server to decrypt, returns true or false for valid or invalid padding"""

def recover_dec_block(iv, block):
    iv_ = bytearray(iv)
    dec_block = bytearray(bytes(16))
    for i in range(15, -1, -1):
        for x in tqdm(range(257), leave=False, desc=f"Byte {i}/16"):
            if x == 256:
                raise Exception('ATTACK FAILED')
            iv_[i] = x
            if oracle(bytes(iv_) + bytes(block)):
                dec_block[i] = x ^ (16 - i)
                for j in range(i, 16):
                    iv_[j] = dec_block[j] ^ (16 - i + 1)
                break
    return dec_block

IV = # given or self defined IV

target = pad(b"message to forge", 16) # MESSAGE TO FORGE SERVER SIDE
target_blocks = [target[_:_+16] for _ in range(0, len(target), 16)]

payload = [b'' for _ in range(len(target_blocks)+1)]
payload[-1] = os.urandom(16)

for i in range(len(target_blocks)-1, -1, -1):
    payload[i] = xor(recover_dec_block(IV, payload[i+1]), target_blocks[i])

final_payload = b''.join(_ for _ in payload)
forged_IV = final_payload[:16]
forged_CT = final_payload[16:]
# send according to challenge

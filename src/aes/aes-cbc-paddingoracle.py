ct = # ciphertext in bytes
IV = # iv in bytes

def oracle(ciphertext):
    """sends ciphertext to server to decrypt and returns True or False based on valid or invalid padding"""

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
        

# ct_blocks = [IV] + [ct[i:i+16] for i in range(0, len(ct), 16)]
# nblocks = len(ct_blocks) - 1

# blocks = []
# for iv, block in zip(ct_blocks[:-1], ct_blocks[1:]):
#     dec_bloc = recover_dec_block(iv, block)
#     blocks.append(xor(dec_bloc, iv))

#     print(blocks)

# print(b''.join(x for x in blocks))

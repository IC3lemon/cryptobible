from Crypto.Cipher import AES

ciphertext = "ciphertext in hex"
key = "key in hex"

def decrypt(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(key)

    cipher = AES.new(key, AES.MODE_ECB) # change param2 for mode changing. 3rd param for iv/nonce
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

flag = decrypt(ciphertext, key)

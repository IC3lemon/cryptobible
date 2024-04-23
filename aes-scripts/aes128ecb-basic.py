from Crypto.Cipher import AES

#  ----------AES ECB MODE----------

#  Thine must have pycryptodome module installed for this to worketh.

ciphertext = "THINE_CIPHERTEXT_IN_HEX"
key = "THINE_KEY_IN_HEX"

def decrypt(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(key)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

flag = decrypt(ciphertext, key)     # THINE FLAG

def bytes_to_long(b: bytes):
    return int.from_bytes(b)

def long_to_bytes(i: int):
    bits = i.bit_length()
    return i.to_bytes((bits + 7) // 8)

def test():
    m = b"This is a message"
    print(f"Initial message: {m}")
    i = bytes_to_long(m)
    print(f"Converted to int: {i}")
    m = long_to_bytes(i)
    print(f"Converted back to bytes: {m}")

if __name__ == '__main__':
    test()

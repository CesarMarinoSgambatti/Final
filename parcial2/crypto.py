BEGIN_ASCII_PRINTABLE = 32
END_ASCII_PRINTABLE = 126
LEN_ASCII_PRINTABLE = END_ASCII_PRINTABLE - BEGIN_ASCII_PRINTABLE + 1

def cesar_encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + key - BEGIN_ASCII_PRINTABLE) % LEN_ASCII_PRINTABLE + BEGIN_ASCII_PRINTABLE)
    return result

def cesar_decrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) - key - BEGIN_ASCII_PRINTABLE) % LEN_ASCII_PRINTABLE + BEGIN_ASCII_PRINTABLE)
    return result

def xor_encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result

def xor_decrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result

if __name__ == "__main__":
    print("Cesar")
    print("Encrypt: " + cesar_encrypt("Hello World", 3))
    print("Decrypt: " + cesar_decrypt(cesar_encrypt("Hello World", 3), 3))
    print("XOR")
    print("Encrypt: " + xor_encrypt("Lorem Ipsum dolor sit amet", "KEYdos"))
    print("Decrypt: " + xor_decrypt(xor_encrypt("Lorem Ipsum dolor sit amet", "KEYdos"), "KEYdos"))
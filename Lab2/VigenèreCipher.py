import string

alphabet = string.ascii_lowercase


def encrypt(plaintext, key):
    ciphertext = ""
    i = 0
    for c in plaintext:
        if c in alphabet:
            index = alphabet.index(c)
            keyIndex = alphabet.index(key[i % len(key)])
            newIndex = (index + keyIndex) % 26
            ciphertext += alphabet[newIndex]
            i += 1
        else:
            ciphertext += c
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    i = 0
    for c in ciphertext:
        if c in alphabet:
            index = alphabet.index(c)
            keyIndex = alphabet.index(key[i % len(key)])
            newIndex = (index - keyIndex) % 26
            plaintext += alphabet[newIndex]
            i += 1
        else:
            plaintext += c
    return plaintext


option = '0'
while option != 'q':
    print("1. Encrypt\n"
          "2. Decrypt\n"
          "q. Quit")
    option = str(input("Choose an option: "))
    if option == '1':
        plaintext = str(input("Enter a message: ")).lower()
        key = str(input("Enter a key: ")).lower()
        ciphertext = encrypt(plaintext, key)
        print("Encrypted message:\n" + ciphertext)
    if option == '2':
        ciphertext = str(input("Enter a message: ")).lower()
        key = str(input("Enter a key: ")).lower()
        plaintext = decrypt(ciphertext, key)
        print("Decrypted message:\n" + plaintext)

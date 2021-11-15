import string

alphabet = string.ascii_lowercase


def encrypt(plaintext: str, key: int):
    ciphertext = ""
    for c in plaintext:
        if c in alphabet:
            index = alphabet.index(c)
            newIndex = (index + key) % 26
            ciphertext += alphabet[newIndex]
        else:
            ciphertext += c
    return ciphertext


def decrypt(ciphertext: str, key: int):
    plaintext = ""
    for c in ciphertext:
        if c in alphabet:
            index = alphabet.index(c)
            newIndex = (index - key) % 26
            plaintext += alphabet[newIndex]
        else:
            plaintext += c
    return plaintext


def get_key_by_frequency_analysis(text):
    letter_count = {}
    for c in text:
        if c in alphabet:
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1
    most_common_letter = max(letter_count, key=letter_count.get)
    key = abs(alphabet.index('e') - alphabet.index(most_common_letter))
    return key


option = '0'
while option != 'q':
    print("1. Encrypt\n"
          "2. Decrypt\n"
          "q. Quit")
    option = str(input("Choose an option: "))
    if option == '1':
        plaintext = str(input("Enter a message: ")).lower()
        key = int(input("Enter a key: "))
        ciphertext = encrypt(plaintext, key)
        print(f"Encrypted message:{ciphertext}\n")
    elif option == '2':
        ciphertext = str(input("Enter a message: ")).lower()
        key = get_key_by_frequency_analysis(ciphertext)
        plaintext = decrypt(ciphertext, key)
        print(f"Key: {key}\n")
        print(f"Decrypted message: {plaintext}\n")

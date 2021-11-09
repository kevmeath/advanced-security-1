import string

alphabet = string.ascii_lowercase


def encrypt(plaintext, key):
    plaintextMatrix = get_matrix(plaintext)
    keyMatrix = get_matrix(key)
    cipherMatrix = multiply_matrix(keyMatrix, plaintextMatrix)
    ciphertext = ""
    for i in range(2):
        for j in range(2):
            ciphertext += alphabet[cipherMatrix[i][j] % 26]
    return ciphertext


def get_matrix(message):
    matrix = [[0, 0],
              [0, 0]]
    for i in range(2):
        for j in range(2):
            matrix[i][j] = alphabet.index(message[(i + j) + 1 * i])
    return matrix


def multiply_matrix(matrix1, matrix2):
    result = [[0] * 2 for i in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


plaintext = str(input("Enter a message: ")).lower()
key = str(input("Enter a key: "))
if len(plaintext) != 4 or len(key) != 4:
    print("Message and key must be 4 characters each")
else:
    cipher = encrypt(plaintext, key)
    print("Encrypted message: ")
    print(cipher)

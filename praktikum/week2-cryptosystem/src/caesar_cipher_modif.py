# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        elif char.isdigit():
            result += chr((ord(char) - 48 + key) % 10 + 48)  # 48 = ASCII '0'
        else:
            result += char
    return result


def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        elif char.isdigit():
            result += chr((ord(char) - 48 - key) % 10 + 48)
        else:
            result += char
    return result


if __name__ == "__main__":
    message = "Laili Meifa Ayuningtias - 230320557"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("===== Caesar Cipher =====")

    message = input("Enter message: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)


if __name__ == "__main__":
    main()
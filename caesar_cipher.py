def encrypt_file():
    try:
        input_file = input("Enter input file name: ")
        output_file = input("Enter output file name: ")
        key = int(input("Enter encryption key: "))  # Get numeric key
        with open(input_file, "r") as file:
            text = file.read()

        cipher_text = ""

        for ch in text:
            if ch.isalpha():  # Encrypt only letters
                base = ord('A') if ch.isupper() else ord('a')
                cipher_text += chr((ord(ch) - base + key) % 26 + base)
            else:
                cipher_text += ch  # Leave other characters unchanged

        with open(output_file, "w") as file:
            file.write(cipher_text)

        print("File encrypted successfully.")

    except FileNotFoundError:
        print("Input file not found.")
    except ValueError:
        print("Invalid key. Please enter a number.")


def decrypt_file():
    try:
        input_file = input("Enter encrypted file name: ")
        output_file = input("Enter output file name: ")
        key = int(input("Enter decryption key: "))
        with open(input_file, "r") as file:
            text = file.read()

        plain_text = ""

        for ch in text:
            if ch.isalpha():  # Decrypt only letters
                base = ord('A') if ch.isupper() else ord('a')
                plain_text += chr((ord(ch) - base - key) % 26 + base)
            else:
                plain_text += ch

        with open(output_file, "w") as file:
            file.write(plain_text)

        print("File decrypted successfully.")

    except FileNotFoundError:
        print("Encrypted file not found.")
    except ValueError:
        print("Invalid key. Please enter a number.")


# Main
while True:
    print("\nFile Encryption / Decryption")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        encrypt_file()
    elif choice == "2":
        decrypt_file()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")

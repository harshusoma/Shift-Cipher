from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives import padding


# Use the substitution cipher (Shift Cipher) function to encode
def shift_cipher_encrypt(pt, ky):
    encryption_txt = ""
    for char in pt:
        if char.isalpha():
            shift = ord(ky) - ord('A')
            encryption_txt += chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
        else:
            encryption_txt += char
    return encryption_txt

# Use of a substitution cipher (Shift Cipher) to decipher
def shift_cipher_decrypt(ciphertext, ky):
    decryption_txt = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(ky) - ord('A')
            decryption_txt += chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
        else:
            decryption_txt += char
    return decryption_txt

# Encryption method using Vigenere Cipher
def vigenere_cipher_encrypt(pt, ky):
    ky_length = len(ky)
    encryption_txt = ""
    for i in range(len(pt)):
        char = pt[i]
        if char.isalpha():
            shift = ord(ky[i % ky_length].upper()) - ord('A')
            encryption_txt += chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
        else:
            encryption_txt += char
    return encryption_txt

# Decryption method using Vigenere Cipher
def vigenere_cipher_decrypt(ciphertext, ky):
    ky_length = len(ky)
    decryption_txt = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(ky[i % ky_length].upper()) - ord('A')
            decryption_txt += chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
        else:
            decryption_txt += char
    return decryption_txt

# Encryption of the message using AES encryption Algorithm with specific modes
def aes_encrypt(pt, ky, mode):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(ky), mode, backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_pt = padder.update(pt) + padder.finalize()
    ciphertext = encryptor.update(padded_pt) + encryptor.finalize()
    return ciphertext

# Decryption of the message using AES encryption Algorithm with specific modes
def aes_decrypt(ciphertext, ky, mode):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(ky), mode, backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    pt = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_pt = unpadder.update(pt) + unpadder.finalize()
    return unpadded_pt

# Options and function to run the program
def main():
    print("Choose the below options for the specific encryption:")
    print("Select an option for the encryption techniques or methods:")
    print("1. Substitution Cipher (Shift Cipher):")
    print("2. Vigenere Cipher:")
    print("3. AES Encryption Method:")
    
    choice = input("Enter your preferred choice: ")
    
    if choice == "1":
        pt = input("Enter the message which should be encrypted: ")
        ky = input("Enter the encryption key (a letter from A to Z): ").upper()
        ciphertext = shift_cipher_encrypt(pt, ky)
        print("Encrypted message:", ciphertext)
        
        decrypt_choice = input("Do you want the decryption of the message? (yes/no): ")
        if decrypt_choice.lower() == "yes":
            decryption_ky = input("Enter the decryption ky (same as encryption ky): ").upper()
            decryption_txt = shift_cipher_decrypt(ciphertext, decryption_ky)
            print("Decrypted message:", decryption_txt)
    
    elif choice == "2":
        pt = input("Enter the message which should be encrypted: ")
        ky = input("Enter the encryption ky: ")
        ciphertext = vigenere_cipher_encrypt(pt, ky)
        print("Encrypted message:", ciphertext)
        
        decrypt_choice = input("Do you want the decryption of the message? (yes/no): ")
        if decrypt_choice.lower() == "yes":
            decryption_ky = input("Enter the decryption ky (same as encryption ky): ")
            decryption_txt = vigenere_cipher_decrypt(ciphertext, decryption_ky)
            print("Decrypted message:", decryption_txt)
    
    elif choice == "3":
        print("Choose one of the encryption mode:")
        print("1. ECB method:")
        print("2. CBC method:")
        print("3. CFB method:")
        print("4. OFB method:")
        mode_choice = input("Enter the mode: ")

        # options for the user to enter the key
        ky = input("Enter the encryption ky (16 bytes): ").encode()

        if mode_choice == "1":
            mode = modes.ECB()
        elif mode_choice == "2":
            iv = input("Enter the initialization vector (IV) (16 bytes): ").encode()
            mode = modes.CBC(iv)
        elif mode_choice == "3":
            iv = input("Enter the initialization vector (IV) (16 bytes): ").encode()
            mode = modes.CFB(iv)
        elif mode_choice == "4":
            iv = input("Enter the initialization vector (IV) (16 bytes): ").encode()
            mode = modes.OFB(iv)
        else:
            print("Invalid mode choice.")
            return

        pt = input("Enter the message which should be encrypted: ").encode()
        ciphertext = aes_encrypt(pt, ky, mode)
        print("Encrypted message:", base64.b64encode(ciphertext).decode())

        decrypt_choice = input("Do you want the decryption of the message? (yes/no): ")
        if decrypt_choice.lower() == "yes":
            # Should use the same key for decryption
            decryption_ky = ky  
            decryption_txt = aes_decrypt(ciphertext, decryption_ky, mode).decode()
            print("Decrypted message:", decryption_txt)
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

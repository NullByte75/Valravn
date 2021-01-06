import os
from cryptography.fernet import Fernet
import re
from pathlib import Path

def decrypt(key, filename):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def main():
    file = input("Enter file to decrypt>>> ")
    key = input(str("Enter key for decryption>>>")) # you get it from the webhook
    decrypt(key,file)
    print("Done!")
    print("Do you want to decrypt again?")
    choice = input(str("1: Yes\n2: No\n>>>"))
    if choice == "1":
        main()
    if choice == "2":
        print("Exiting...")
        exit()
    else:
        print("Unknown choice exiting...")
        exit()

main()

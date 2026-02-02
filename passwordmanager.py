from cryptography.fernet import Fernet

password=input("what is the master password: ")

import os

def generate_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        generate_key()
    with open("key.key","rb") as file:  # rb is read binary
        key=file.read()
    return key

key=load_key() 
fer=Fernet(key)

def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords stored yet.")
        return
    with open('passwords.txt','r') as f:
        for line in f:
            data=line.rstrip()
            if not data or "|" not in data:
                continue
            user,passw = data.split("|", 1)
            try:
                password = fer.decrypt(passw.encode()).decode()
            except Exception as e:
                password = f"<decryption error: {e}>"
            print("User:", user, "| Password:", password)
def add():
    name=input("Account Name: ")
    pwd=input("Password: ")
    with open('passwords.txt','a') as f: #a is the append mode
        f.write(name + "|" +(fer.encrypt(pwd.encode()).decode()) + "\n")
while True:
    mode=input("would you like to add a new password or view existing ones (view/add)?,press q to quit: ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
        continue
print("bye!")
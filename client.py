import socket
import threading
import stdiomask

HOST = "127.0.0.1"
PORT = 20202
FORMAT = "utf8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def signUp():
    print("[REGISTER]")

    #client nhap username
    user = input("input username:")
    client.sendall(user.encode(FORMAT))

    #cho server response
    msg = client.recv(1024).decode(FORMAT)
    if msg == "existed":
        while msg == "existed":
            user = input("try another username:")
            client.sendall(user.encode(FORMAT))
            msg = client.recv(1024).decode(FORMAT)
            if msg == "ready":
                break

    psw = stdiomask.getpass("input password :")
    client.sendall(psw.encode(FORMAT))

    print("sign up successfully")


def login():
    print("[LOGIN]")
    user = input("input username :")
    client.sendall(user.encode(FORMAT))

    msg = client.recv(1024).decode(FORMAT)
    if msg == "not existed":
        while msg == "not existed":
            user = input("not existed username, input again: ")
            client.sendall(user.encode(FORMAT))
            msg = client.recv(1024).decode(FORMAT)
            if msg == "ready":
                break

    psw = stdiomask.getpass("input password :")
    client.sendall(psw.encode(FORMAT))

    msg = client.recv(1024).decode(FORMAT)
    if msg == "err":
        while msg == "err":
            psw = stdiomask.getpass("wrong password, input password again :")
            client.sendall(psw.encode(FORMAT))
            msg = client.recv(1024).decode(FORMAT)
            if msg == "ready":
                break
    print("[LOGIN] success")

login()













import socket
import threading

HOST = "127.0.0.1"
PORT = 20202
FORMAT = "utf8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def signUp():
    #client nhap username
    user = input("input username:")
    client.sendall(user.encode(FORMAT))

    msg = client.recv(1024).decode(FORMAT)
    if msg == "existed":
        while msg == "existed":
            user = input("try another username:")
            client.sendall(user.encode(FORMAT))
            msg = client.recv(1024).decode(FORMAT)
            if msg == "1":
                break

    psw = input("input password :")
    client.sendall(psw.encode(FORMAT))

    print("sign up successfully")


signUp()
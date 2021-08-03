import socket
import threading
import db as db

HOST = "127.0.0.1"
PORT = 20202
FORMAT = "utf8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

online= []

print("server is listening")

def signUp():
    conn, addr = s.accept()
    user = conn.recv(1024).decode(FORMAT)
    #check database
    check = db.check_user_existed(user)
    if check:
        while check:
            conn.send("existed".encode(FORMAT))
            user = conn.recv(1024).decode(FORMAT)
            if not db.check_user_existed(user):
                conn.send("1".encode(FORMAT))
                break
            else:
                check = True
    else:
        conn.send("psw".encode(FORMAT))

    psw = conn.recv(1024).decode(FORMAT)

    db.insert_data(user, psw)

signUp()






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
conn, addr = s.accept()

def signUp():
    user = conn.recv(1024).decode(FORMAT)

    #check database
    check = db.check_user_existed(user)
    if check:
        while check:
            conn.send("existed".encode(FORMAT))
            user = conn.recv(1024).decode(FORMAT)
            if not db.check_user_existed(user):
                conn.send("ready".encode(FORMAT))
                break
            else:
                check = True
    else:
        conn.send("psw".encode(FORMAT))

    psw = conn.recv(1024).decode(FORMAT)

    db.insert_data(user, psw)


def login():
    user = conn.recv(1024).decode(FORMAT)

    #check database
    existed = db.check_user_existed(user)

    if not existed:
        while not existed:
            conn.send("not existed".encode(FORMAT))
            user = conn.recv(1024).decode(FORMAT)
            if db.check_user_existed(user):
                conn.send("ready".encode(FORMAT))
                break
            else:
                existed = False
    else:
        conn.send("psw".encode(FORMAT))

    psw = conn.recv(1024).decode(FORMAT)

    match = db.check_pass(user, psw)

    if match:
        conn.sendall("success".encode(FORMAT))
    else:
        while not match:
            conn.send("err".encode(FORMAT))
            psw = conn.recv(1024).decode(FORMAT)
            if db.check_pass(user, psw):
                conn.send("ready".encode(FORMAT))
                online.append(user)
                break
            else:
                match = False
    print(user, psw)

def change_password():
    user = conn.recv(1024).decode(FORMAT)

    # check database
    existed = db.check_user_existed(user)

    if not existed:
        while not existed:
            conn.send("not existed".encode(FORMAT))
            user = conn.recv(1024).decode(FORMAT)
            if db.check_user_existed(user):
                conn.send("ready".encode(FORMAT))
                break
            else:
                existed = False
    else:
        conn.send("psw".encode(FORMAT))

    psw = conn.recv(1024).decode(FORMAT)

    match = db.check_pass(user, psw)

    if match:
        conn.sendall("success".encode(FORMAT))
    else:
        while not match:
            conn.send("err".encode(FORMAT))
            psw = conn.recv(1024).decode(FORMAT)
            if db.check_pass(user, psw):
                conn.send("ready".encode(FORMAT))
                online.append(user)
                break
            else:
                match = False

    new_psw = conn.recv(1024).decode(FORMAT)
    db.update_info('password', user, new_psw)





change_password()












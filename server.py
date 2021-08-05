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

def signUp(conn):
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


def login(conn):
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


def change_password(conn):
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

def check_user(conn):
    user = conn.recv(1024).decode(FORMAT)

    # check database
    existed = db.check_user_existed(user)
    if not existed:
        conn.send("not existed".encode(FORMAT))
    else:
        conn.send("existed".encode(FORMAT))
        opt = conn.recv(1024).decode(FORMAT)
        if opt == '-find':
            name = conn.recv(1024).decode(FORMAT)
            if db.check_user_existed(name):
                conn.send(f"account named {name} existed".encode(FORMAT))
            else:
                conn.send(f"account named {name} not existed".encode(FORMAT))

        else:
            result = db.check_user_info(opt, user)
            conn.sendall(result.encode(FORMAT))


def setup_info(conn, user):
    opt = conn.recv(1024).decode(FORMAT)

    if opt == '-fullname':
        change = conn.recv(1024).decode(FORMAT)
        db.update_info('fullname', user, change)

    elif opt == '-date':
        change = conn.recv(1024).decode(FORMAT)
        db.update_info('dob', user, change)

    elif opt == '-note':
        change = conn.recv(1024).decode(FORMAT)
        db.update_info('note', user, change)


def handle_client(conn, addr):
    while True:
        try:
            option = conn.recv(1024).decode(FORMAT)

            if option == 'login':
                login(conn)

            elif option == 'signup':
                signUp(conn)

            elif option == 'changepass':
                change_password(conn)

            elif option == 'checkuser':
                check_user(conn)

            elif option == 'setupinfo':
                user = 'hoang'
                setup_info(conn, user)

            elif option == 'quit':
                print(f"disconnected from {addr}")
                conn.close()
                break

        except:
            print(f"disconected from {addr} ")
            break
    conn.close()


def runServer():
    try:
        print("server is listening")
        while True:
            conn, addr = s.accept()
            print(f"connected with address :{addr}")
            clientThread = threading.Thread(target=handle_client, args=(conn, addr))
            clientThread.start()
    except :
        print("failed to connected to client")

    finally:
        s.close()
        print("end")


sThread = threading.Thread(target=runServer)
sThread.start()
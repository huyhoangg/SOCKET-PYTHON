import socket
import threading
import db as db

HOST = "127.0.0.1"
PORT = 20202
FORMAT = "utf8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

online = []
id = []

def isOnline(online, name):
    for i in range(len(online)):
        if online[i] == name:
            return True
    return False

def remove_online(addr):
    s = str(addr)
    for i in range(len(id)):
        account = id[i].split('-')
        if account[0] == s:
            name = account[1]
            id.pop(i)
            online.remove(name)
            break

def add_id(user, addr):
    s = str(addr) + '-' + user
    id.append(s)
    online.append(user)


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

def checkdata(conn):
    user = conn.recv(1024).decode(FORMAT)
    existed = db.check_user_existed(user)
    if existed:
        conn.send("true".encode(FORMAT))
    else:
        conn.send("false".encode(FORMAT))

def login(conn, addr):
    user = conn.recv(1024).decode(FORMAT)
    print(user)

    conn.send("a".encode(FORMAT))

    psw = conn.recv(1024).decode(FORMAT)
    print(psw)
    match = db.check_pass(user, psw)
    print(match)
    if match:
        conn.sendall("success".encode(FORMAT))
        add_id(user, addr)
    else:
        conn.sendall("error".encode(FORMAT))

        # while not match:
        #     conn.send("err".encode(FORMAT))
        #     psw = conn.recv(1024).decode(FORMAT)
        #     if db.check_pass(user, psw):
        #         conn.send("ready".encode(FORMAT))
        #         add_id(user, addr)
        #         break
        #     else:
        #         match = False


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
            if db.check_user_existed(user):
                conn.send(f"account named {user} existed".encode(FORMAT))
            else:
                conn.send(f"account named {user} not existed".encode(FORMAT))
        elif opt == '-online':
            if isOnline(online, user):
                conn.send(f"{user} now online".encode(FORMAT))
            else:
                conn.send(f"{user} not active".encode(FORMAT))

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
                login(conn, addr)

            elif option == 'checkdata':
                checkdata(conn)

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
                remove_online(addr)
                conn.close()
                break

        except:
            print(f"disconected from {addr} ")
            remove_online(addr)
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
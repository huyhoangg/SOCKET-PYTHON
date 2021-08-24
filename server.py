import socket
import threading
import db as db
import game as game

HOST = "127.0.0.1"
PORT = 20202
FORMAT = "utf8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

online = []
id = []

clients = {}

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

    conn.send("a".encode(FORMAT))
    psw = conn.recv(1024).decode(FORMAT)

    db.insert_data(user, psw)

def checkdata(conn):
    user = conn.recv(1024).decode(FORMAT)
    existed = db.check_user_existed(user)
    if existed:
        conn.send("true".encode(FORMAT))
    else:
        conn.send("false".encode(FORMAT))

def checkpass(conn):
    conn.send("h".encode(FORMAT))
    user = conn.recv(1024).decode(FORMAT)

    conn.send("h".encode(FORMAT))
    oldPass = conn.recv(1024).decode(FORMAT)

    check = db.check_pass(user, oldPass)
    if check:
        conn.send("true".encode(FORMAT))
    else:
        conn.send("false".encode(FORMAT))

def login(conn, addr):
    user = conn.recv(1024).decode(FORMAT)

    conn.send("a".encode(FORMAT))

    psw = conn.recv(1024).decode(FORMAT)
    match = db.check_pass(user, psw)
    if match:
        conn.sendall("success".encode(FORMAT))
        add_id(user, addr)
        clients[conn] = user
    else:
        conn.sendall("error".encode(FORMAT))



def change_password(conn):
    conn.send("h".encode(FORMAT))
    user = conn.recv(1024).decode(FORMAT)
    conn.send("h".encode(FORMAT))


    new_psw = conn.recv(1024).decode(FORMAT)
    db.update_info('password', user, new_psw)

def check_user(conn):

    conn.send("2".encode(FORMAT))
    user = conn.recv(1024).decode(FORMAT)
    conn.send("1".encode(FORMAT))

    opt = conn.recv(1024).decode(FORMAT)

    if opt == '-online':
        if isOnline(online, user):
            conn.send(f"{user} now online".encode(FORMAT))
        else:
            conn.send(f"{user} not active".encode(FORMAT))

    else:
        result = db.check_user_info(opt, user)
        conn.sendall(result.encode(FORMAT))


def setup_info(conn, user):
    conn.send("a".encode(FORMAT))
    opt = conn.recv(1024).decode(FORMAT)

    if opt == '-fullname':
        conn.send("a".encode(FORMAT))

        change = conn.recv(1024).decode(FORMAT)
        db.update_info('fullname', user, change)

    elif opt == '-date':
        conn.send("a".encode(FORMAT))

        change = conn.recv(1024).decode(FORMAT)
        db.update_info('dob', user, change)

    elif opt == '-note':
        conn.send("a".encode(FORMAT))

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

            elif option == 'checkpass':
                checkpass(conn)

            elif option == 'signup':
                signUp(conn)

            elif option == 'changepass':
                change_password(conn)

            elif option == 'checkuser':
                check_user(conn)

            elif option == 'setupinfo':
                conn.send("1".encode(FORMAT))
                user = conn.recv(1024).decode(FORMAT)
                setup_info(conn, user)

            elif option == 'showList':
                conn.send("1".encode(FORMAT))

                s = f"list user online: {online}"
                conn.send(s.encode(FORMAT))

            elif option == 'invite':
                conn.send("1".encode(FORMAT))

                user = conn.recv(1024).decode(FORMAT)
                conn.send("1".encode(FORMAT))

                fr = conn.recv(1024).decode(FORMAT)
                for client in clients:
                    if (clients[client] == fr):
                        client.send(f"[INVITATION] {user} invite you to game".encode(FORMAT))
                        print('x')

            elif option == 'upload':
                conn.send("1".encode(FORMAT))
                path = conn.recv(1024).decode(FORMAT)
                conn.send("1".encode(FORMAT))
                user = conn.recv(1024).decode(FORMAT)

                datamap = game.read_map(path)
                game.addMap(user, datamap)


            elif option == 'quit':
                print(f"disconnected from {addr}")
                remove_online(addr)
                del clients[conn]
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
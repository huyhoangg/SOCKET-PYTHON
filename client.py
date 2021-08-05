import socket
import threading
import stdiomask

HOST = "127.0.0.1"
PORT = 20202
FORMAT = "utf8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def signUp(client):
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

    print("[SIGN_UP] successfully")


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


def change_password(client):
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

    psw = stdiomask.getpass("input last password :")
    client.sendall(psw.encode(FORMAT))

    msg = client.recv(1024).decode(FORMAT)
    if msg == "err":
        while msg == "err":
            psw = stdiomask.getpass("wrong password, input password again :")
            client.sendall(psw.encode(FORMAT))
            msg = client.recv(1024).decode(FORMAT)
            if msg == "ready":
                break

    new_psw = stdiomask.getpass("input your new password :")
    client.sendall(new_psw.encode(FORMAT))
    print("[PASSWORD] successfully changed")


def check_user(client):
    print("[USER CHECK]")
    user = input("input username :")
    client.sendall(user.encode(FORMAT))

    msg = client.recv(1024).decode(FORMAT)
    if msg == "not existed":
        print("not existed user")
        client.close()
    else:
        print("option : [-find] [-online] [-show_date] [-show_fullname] "
              "[-show_note] [-show_all] [-show_point]")
        type = input("choice :")

        if type == '-show_fullname':
            client.sendall(type.encode(FORMAT))
        elif type == '-show_date':
            client.sendall(type.encode(FORMAT))
        elif type == '-show_note':
            client.sendall(type.encode(FORMAT))
        elif type == '-show_point':
            client.sendall(type.encode(FORMAT))
        elif type == '-show_all':
            client.sendall(type.encode(FORMAT))
        elif type == '-find':
            client.sendall(type.encode(FORMAT))
            name = input("input someone :")
            client.sendall(name.encode(FORMAT))
        elif type == "-online":
            pass

        else:
            print("not regconised command")
            client.close()

        result = client.recv(1024).decode(FORMAT)
        print(result)

def setup_info(client, user):
    print("option : [-fullname] [-date] [-note]")
    opt = input("chose option :")

    if opt == "-fullname":
        client.sendall(opt.encode(FORMAT))
        change = input("update fullname :")
        client.sendall(change.encode(FORMAT))
        print("[USER] information changed")

    elif opt == "-date":
        client.sendall(opt.encode(FORMAT))
        change = input("update date of birth (dd/mm/yy) :")
        client.sendall(change.encode(FORMAT))
        print("[USER] information changed")

    elif opt == "-note":
        client.sendall(opt.encode(FORMAT))
        change = input("update some note :")
        client.sendall(change.encode(FORMAT))
        print("[USER] information changed")

    else:
        print("not valid command")


def run_client():

    while True:
        print("option : [login] [signup] [changepass] "
              "[checkuser] [setupinfo] [quit]")
        opt = input("choice :")
        client.sendall(opt.encode(FORMAT))

        if opt == 'login':
            login()

        elif opt == 'signup' :
            signUp(client)

        elif opt == 'changepass':
            change_password(client)

        elif opt == 'checkuser':
            check_user(client)

        elif opt == 'setupinfo':
            user = 'hoang'
            setup_info(client, user)

        elif opt == 'quit':
            print("byebye")
            client.close()
            break

run_client()
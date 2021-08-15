import socket
import threading
import stdiomask
from tkinter import *


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
    print("[USER CHECKING PLACE]")
    user = input("Who are you looking for :")
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

        elif type == "-online":
            client.sendall(type.encode(FORMAT))

        else:
            print('not valid command')
            client.close()
            return

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


def register():
    global screenRegis
    screenRegis = Toplevel(screen)
    screenRegis.title("Register")
    screenRegis.geometry("400x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screenRegis, text="Register Form", bg="grey", font=("Calibri", 13), width="25").pack()
    Label(screenRegis, text="").pack()
    Label(screenRegis, text="").pack()

    username_lable = Label(screenRegis, text="Username  ")
    username_lable.pack()

    username_entry = Entry(screenRegis, textvariable=username, width="25")
    username_entry.pack()
    Label(screenRegis, text="").pack()

    password_lable = Label(screenRegis, text="Password  ")

    password_lable.pack()
    password_entry = Entry(screenRegis, textvariable=password, width="25")
    password_entry.pack()
    password_lable.pack()
    Label(screenRegis, text="").pack()
    Button(screenRegis, text="Register", width=10, height=1, bg="#0d8bf0", fg="black").pack()

def checkuser():
    client.sendall("checkdata".encode(FORMAT))

    user = usernameLogin.get()
    client.sendall(user.encode(FORMAT))
    check = client.recv(1024).decode(FORMAT)
    if check == "false":
        Label(screenLogin, text="Account not found",fg="red", font=("Calibri", 10), width="25").place(x=100, y=90)
    else:
        Label(screenLogin, text="Account found",fg="green", font=("Calibri", 10), width="25").place(x=100, y=90)
        b["state"] = "normal"

def validate():
    client.send("login".encode(FORMAT))

    user = usernameLogin.get()
    psw = passwordLogin.get()

    client.send(user.encode(FORMAT))
    client.recv(1024)
    client.send(psw.encode(FORMAT))
    msg = client.recv(1024).decode()
    if msg == "success":
        Label(screenLogin, text="Login success",fg="green", font=("Calibri", 13), width="25").place(x=90, y=200)
    else:
        Label(screenLogin, text="Wrong password",fg="red", font=("Calibri", 13), width="25").place(x=90, y=200)

def login1():
    global screenLogin
    screenLogin = Toplevel(screen)
    screenLogin.title("Login")
    screenLogin.geometry("400x300")

    global usernameLogin
    global passwordLogin

    usernameLogin = StringVar()
    passwordLogin = StringVar()

    global username_entry1
    global password_entry1

    Label(screenLogin, text="Login", bg="grey", font=("Calibri", 13), width="25").pack()
    Label(screenLogin, text="").pack()
    Label(screenLogin, text="Username ").pack()
    username_entry1 = Entry(screenLogin, textvariable=usernameLogin, width="25")
    username_entry1.pack()
    Button(screenLogin, text = "Check", command=checkuser).place(x= 300, y=66)

    Label(screenLogin, text="").pack()
    Label(screenLogin, text="Password  ").pack()
    password_entry1 = Entry(screenLogin, textvariable=passwordLogin, width="25", show ="*")
    password_entry1.pack()
    Label(screenLogin, text="").pack()

    global b
    b= Button(screenLogin, text="Login",state="disabled", width=10, height=1, bg="black", fg="white", command = validate)
    b.pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x300")
    screen.title("Account Login")
    Label(text="Select Your Choice", bg="#f96854", width="300", height="2", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="35", command=login1).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="35", command=register).pack()
    Label(text="").pack()

    screen.mainloop()


main_screen()

import socket
import threading
import tkinter.messagebox

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

def checkpass(user):
    client.sendall("checkpass".encode(FORMAT))
    oldpass = oldPass.get()

    client.recv(1024)

    client.sendall(user.encode(FORMAT))
    client.recv(1024)

    client.sendall(oldpass.encode(FORMAT))

    check = client.recv(1024).decode(FORMAT)
    if check == "false":
        Label(passScreen, text="Password not match", fg="red", font=("Calibri", 10), width="25").place(x=100, y=90)
    else:
        Label(passScreen, text="Password true !", fg="green", font=("Calibri", 10), width="25").place(x=100, y=90)
        changepassBut["state"] = "normal"

def changePass(user):
    client.sendall("changepass".encode(FORMAT))
    newpass = newPass.get()

    client.recv(1024)

    client.sendall(user.encode(FORMAT))
    client.recv(1024)

    client.sendall(newpass.encode(FORMAT))
    Label(passScreen, text="Update success !", fg="green", font=("Calibri", 13), width="25").place(x=90, y=200)


def changepassGUI(user):
    global passScreen
    passScreen = Toplevel(Hscreen)
    passScreen.title("Login")
    passScreen.geometry("400x300")

    global oldPass
    global newPass

    oldPass = StringVar()
    newPass = StringVar()

    global old_entry
    global new_entry

    Label(passScreen, text="Change Password Form", bg="grey", font=("Calibri", 13), width="25").pack()
    Label(passScreen, text="").pack()
    Label(passScreen, text="Old Password ").pack()
    old_entry = Entry(passScreen, textvariable=oldPass,show ="*", width="25")
    old_entry.pack()
    Button(passScreen, text="Check",command=lambda : checkpass(user)).place(x=300, y=66)

    Label(passScreen, text="").pack()
    Label(passScreen, text="New Password ").pack()
    new_entry = Entry(passScreen, textvariable=newPass, width="25", show="*")
    new_entry.pack()
    Label(passScreen, text="").pack()

    global changepassBut
    changepassBut = Button(passScreen, text="Change Password", state="disabled", width=20, height=1, bg="black", fg="white",command = lambda :changePass(user))

    changepassBut.pack()

def updateName(user):
    client.sendall("setupinfo".encode(FORMAT))
    newname = new_name.get()
    client.recv(1024)

    client.sendall(user.encode(FORMAT))

    client.recv(1024)
    client.sendall("-fullname".encode(FORMAT))
    client.recv(1024)
    client.sendall(newname.encode(FORMAT))
    Label(nameScreen, text="Update success !", fg="violetred1", font=("Calibri", 13), width="25").place(x=90, y=150)


def nameGUI(user):
    global nameScreen
    nameScreen = Toplevel(Hscreen)
    nameScreen.title("Login")
    nameScreen.geometry("400x300")

    global new_name
    new_name = StringVar()

    global name_entry

    Label(nameScreen, text="Update Fullname Form", bg="cyan2", font=("Calibri", 13), width="25").pack()
    Label(nameScreen, text="").pack()
    Label(nameScreen, text="What's your name ?").pack()
    name_entry = Entry(nameScreen, textvariable=new_name, width="35")
    name_entry.pack()

    Button(nameScreen, text="Update", width=20, height=1, bg="maroon1", fg="white",command = lambda :updateName(user)).pack(pady= 10)

def updateNote(user):
    client.sendall("setupinfo".encode(FORMAT))
    newnote = note.get()
    client.recv(1024)

    client.sendall(user.encode(FORMAT))

    client.recv(1024)
    client.sendall("-note".encode(FORMAT))
    client.recv(1024)
    client.sendall(newnote.encode(FORMAT))
    Label(noteScr, text="Update success !", fg="violetred1", font=("Calibri", 13), width="25").place(x=90, y=150)


def noteGUI(user):
    global noteScr
    noteScr = Toplevel(Hscreen)
    noteScr.title("Login")
    noteScr.geometry("400x300")
    global note
    note = StringVar()

    global note_entry

    Label(noteScr, text="Update Status ", bg="cyan2", font=("Calibri", 13), width="25").pack()
    Label(noteScr, text="").pack()
    Label(noteScr, text="Tell something ").pack()
    note_entry = Entry(noteScr, textvariable=note, width="35")
    note_entry.pack()

    Button(noteScr, text="Update", width=20, height=1, bg="maroon1", fg="white",command=lambda :updateNote(user)).pack(pady= 10)


def updateBirth(user):
    client.sendall("setupinfo".encode(FORMAT))
    newdob = birth.get()
    client.recv(1024)

    client.sendall(user.encode(FORMAT))

    client.recv(1024)
    client.sendall("-date".encode(FORMAT))
    client.recv(1024)
    client.sendall(newdob.encode(FORMAT))
    Label(birthScreen, text="Update success !", fg="violetred1", font=("Calibri", 13), width="25").place(x=90, y=150)


def birthGUI(user):
    global birthScreen
    birthScreen = Toplevel(Hscreen)
    birthScreen.title("Login")
    birthScreen.geometry("400x300")
    global birth
    birth = StringVar()

    global birth_entry

    Label(birthScreen, text="Update Birthday Form", bg="cyan2", font=("Calibri", 13), width="25").pack()
    Label(birthScreen, text="").pack()
    Label(birthScreen, text="What's your date of birth ?").pack()
    birth_entry = Entry(birthScreen, textvariable=birth, width="35")
    birth_entry.pack()

    Button(birthScreen, text="Update", width=20, height=1, bg="maroon1", fg="white",command=lambda :updateBirth(user)).pack(pady= 10)

def showInfo(opt):
    client.sendall("checkuser".encode(FORMAT))
    client.recv(1024)
    user = who.get()
    client.sendall(user.encode(FORMAT))
    client.recv(1024)

    client.sendall(opt.encode(FORMAT))
    result = client.recv(1024).decode(FORMAT)
    Label(show_note_Scr,text= result, bg="cyan2",fg="black", font=(15)).pack()

def checkuserShow():
    client.sendall("checkdata".encode(FORMAT))

    user = who.get()
    client.sendall(user.encode(FORMAT))
    check = client.recv(1024).decode(FORMAT)
    if check == "false":
        Label(show_note_Scr, text="We cant find this user",fg="red", font=("Calibri", 10), width="25").place(x=100, y=130)
    else:
        Label(show_note_Scr, text="This user is in our game",fg="green", font=("Calibri", 10), width="25").place(x=100, y=130)
        showBut["state"] = "normal"

def showGUI(opt):
    global show_note_Scr
    show_note_Scr = Toplevel(Hscreen)
    show_note_Scr.title("See your friend status ")
    show_note_Scr.geometry("400x300")
    global who
    who = StringVar()

    global who_entry

    Label(show_note_Scr, text="See your friend status ", bg="cyan2", font=("Calibri", 13), width="25").pack()
    Label(show_note_Scr, text="").pack()
    Label(show_note_Scr, text="who are you looking for ").pack()
    who_entry = Entry(show_note_Scr, textvariable=who, width="35")
    who_entry.pack()

    Button(show_note_Scr, text = "Check",command=checkuserShow).place(x= 330, y=64)
    user = who.get()
    global showBut
    showBut= Button(show_note_Scr, text="Watch",state="disable", width=20, height=1, bg="maroon1", fg="white",command=lambda :showInfo(opt))
    showBut.pack(pady=10)

def findShow():
    client.sendall("checkdata".encode(FORMAT))

    user = who.get()
    client.sendall(user.encode(FORMAT))
    check = client.recv(1024).decode(FORMAT)
    if check == "false":
        Label(findS, text="We cant find this user ",fg="red", font=("Calibri", 10), width="30").place(x=80, y=120)
    else:
        Label(findS, text="This user is in our game",fg="maroon1", font=("Calibri", 10), width="27").place(x=80, y=120)

def findGUI():
    global findS
    findS = Toplevel(Hscreen)
    findS.title("Information area ")
    findS.geometry("400x300")
    global who
    who = StringVar()

    global who_entry

    Label(findS, text="Looking for your friend ", bg="cyan2", font=("Calibri", 13), width="25").pack()
    Label(findS, text="").pack()
    Label(findS, text="who are you looking for ").pack()
    who_entry = Entry(findS, textvariable=who, width="35")
    who_entry.pack()

    Button(findS, text = "Check",command=findShow).place(x= 330, y=64)

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        client.sendall("quit".encode(FORMAT))
        Hscreen.destroy()
        client.close()

def homepage(user):
    global Hscreen
    Hscreen = Toplevel(screenLogin)
    Hscreen.geometry("800x600")
    Hscreen.title("Homepage")

    Label(Hscreen,text="Welcome to game, "+user, bg= "MediumOrchid1",fg="turquoise1",font=("Calibri", 19),height=3 ,width=600).pack()
    Label(Hscreen,bg= "purple1",fg="black",height=10 ,width=600).pack()
    Label(Hscreen,bg= "mediumOrchid4",fg="black",height=12 ,width=600).pack()
    Label(Hscreen,bg= "dark slate blue",fg="black",height=10 ,width=600).pack()


    Label(Hscreen,text="Check out your information",bg="PaleVioletRed1",font=("Calibri", 15)).place(x=10,y=110)
    Label(Hscreen,text="Looking for someone ?",bg="tomato2",font=("Calibri", 15)).place(x=10,y=270)

    Button(Hscreen,text="Change Password",bg="darkorchid1",fg="gold", height="2", width="20",command=lambda :changepassGUI(user)).place(x=20, y= 170)
    Button(Hscreen,text="Fullname",bg="darkorchid2",fg="gold", height="2", width="20", command=lambda :nameGUI(user)).place(x=220, y= 170)
    Button(Hscreen,text="Birthday",bg="darkorchid3",fg="gold", height="2", width="20",command=lambda :birthGUI(user)).place(x=420, y= 170)
    Button(Hscreen,text="Note",bg="darkorchid4",fg="gold", height="2", width="20",command=lambda :noteGUI(user)).place(x=620, y= 170)

    Button(Hscreen,text="Show fullname", bg="maroon1",fg="cyan", height="2", width="20",command=lambda :showGUI("-show_fullname")).place(x=20, y=370)
    Button(Hscreen,text="Show birthday", bg="maroon2",fg="cyan", height="2", width="20",command=lambda :showGUI("-show_date")).place(x=220, y=370)
    Button(Hscreen,text="Show point", bg="maroon3",fg="cyan", height="2", width="20",command=lambda :showGUI("-show_point")).place(x=420, y=370)
    Button(Hscreen,text="Show note", bg="violetred3",fg="cyan", height="2", width="20",command=lambda :showGUI("-show_note")).place(x=620, y=370)

    Button(Hscreen,text="Find your friend", bg="maroon2", fg="cyan", height="2", width="20",command = findGUI).place(x=130, y=310)
    Button(Hscreen,text="Find online user", bg="maroon3", fg="cyan", height="2", width="20",command=lambda :showGUI("-online")).place(x=330, y=310)
    Button(Hscreen,text="Show everything", bg="violetred3", fg="cyan", height="2", width="20",command=lambda :showGUI("-show_all")).place(x=530, y=310)

    Hscreen.protocol("WM_DELETE_WINDOW", on_closing)

    Hscreen.mainloop()

def checkuser_R():
    client.sendall("checkdata".encode(FORMAT))

    user = username.get()
    client.sendall(user.encode(FORMAT))
    check = client.recv(1024).decode(FORMAT)
    if check == "false":
        Label(screenRegis, text="This account is ready to use",fg="green", font=("Calibri", 10), width="25").place(x=100, y=110)
        buttonR["state"] = "normal"
    else:
        Label(screenRegis, text="This is an existed account",fg="red", font=("Calibri", 10), width="25").place(x=100, y=110)

def regis():
    client.send("signup".encode(FORMAT))

    user = username.get()
    psw = password.get()

    client.send(user.encode(FORMAT))
    client.recv(1024)
    client.send(psw.encode(FORMAT))
    Label(screenRegis, text="Register successfully", fg="green", font=("Calibri", 10), width="25").place(x=100,y=220)



def register1():
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
    Button(screenRegis, text = "Check", command=checkuser_R).place(x= 300, y=85)

    username_lable = Label(screenRegis, text="Username  ")
    username_lable.pack()

    username_entry = Entry(screenRegis, textvariable=username, width="25")
    username_entry.pack()
    Label(screenRegis, text="").pack()

    password_lable = Label(screenRegis, text="Password  ")

    password_lable.pack()
    password_entry = Entry(screenRegis, textvariable=password,show = "*", width="25")
    password_entry.pack()
    password_lable.pack()
    Label(screenRegis, text="").pack()
    global buttonR
    buttonR = Button(screenRegis, text="Register",state = "disable",command = regis, width=10, height=1, bg="#0d8bf0", fg="black")
    buttonR.pack()

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
        homepage(user)
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
    Button(text="Register", height="2", width="35", command=register1).pack()
    Label(text="").pack()

    screen.mainloop()

main_screen()

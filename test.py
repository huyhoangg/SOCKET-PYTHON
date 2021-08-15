
from tkinter import *
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

def cmd():
    if usernameLogin.get()=="1":
        return True
    else:
        return False

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

    Label(screenLogin, text="").pack()
    Label(screenLogin, text="Password  ").pack()
    password_entry1 = Entry(screenLogin, textvariable=passwordLogin, width="25")
    password_entry1.pack()
    Label(screenLogin, text="").pack()
    b1 = Button(screenLogin, text="Login",state = "disabled", width=10, height=1, bg="black", fg="white", command= cmd).pack()
    b1["state"] = "disabled"


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

